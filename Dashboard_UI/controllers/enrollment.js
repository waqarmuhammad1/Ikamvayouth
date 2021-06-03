$(document).ready(function () {
  $("progress_container").hide();
  document.getElementById("progress_container").style.display = 'none';
  var $branches = $("#branches-select");
  var $schools = $("#schools-select");
  var $select_years_to = $('#select_years_to');
  var $select_years_from = $('#select_years_from');
  var barGraphDiv = document.getElementById("enrollmentBar");
  var barGraphDivAll = document.getElementById("enrollmentBarAll");
  var $data = document.getElementById("data");
  var allschools = [];
  var allbranches = [];
  var allyears = [];
  var config = {
    modeBarButtonsToRemove: ['autoScale2d', 'resetScale2d',
      'hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d'
    ],
    displaylogo: false
  };


  var barLayout;
  $('select').material_select();

  function ajaxCallsFunc(type, url, contentType, data, callback) {
    $.ajax({
      type: type,
      url: url,
      contentType: contentType,
      data: data,
      success: callback
    });
  }

  ajaxCallsFunc('POST', "http://41.164.192.98:5000/Branches", 'application/json', null, function (branches) {
    //console.log(branches);
    $.each(branches, function (i, branch) {
      $branches.append('<option value="' + branch + '">' + branch + '</option>');
      $branches.material_select();
      allbranches.push(branch);
    });
  });
  ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetTimeYears", 'application/json', null, function (years) {
    console.log(years);

    $.each(years, function (i, year) {
      $select_years_to.append('<option value="' + year + '">' + year + '</option>');
      $select_years_to.material_select();
      $select_years_from.append('<option value="' + year + '">' + year + '</option>');
      $select_years_from.material_select();
      allyears.push(year);
    });
  });



  ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetSchools", 'application/json', null, function (schools) {
    //console.log(schools);
    $.each(schools, function (i, school) {
      $schools.append('<option value="' + school + '">' + school + '</option>');
      $schools.material_select();
      allschools.push(school);
    });
  });

  var tempLis2 = [];
  var tempLis = [];
  var branchList = [];
  $("#drawgraph").click(function () {
    document.getElementById("progress_container").style.display = 'block';
    var barLayout2;
    tempLis = [];
    tempLis2 = [];
    var filtertype = $('input[name=group1]:checked').val();
    console.log(filtertype)
    var filterDatetype = $('input[name=time_selection]:checked').val();
    if (filtertype == "Branch") {
      branchList = $("#branches-select").val();
    } else if (filtertype == "allbranches") {
      filtertype = "Branch";
      branchList = allbranches;
      console.log(branchList)
    } else if (filtertype == "School") {
      branchList = $("#schools-select").val();
    } else if (filtertype == "allschools") {
      filtertype = "School";
      branchList = allschools;
    }
    var gradeList = $("#grades-select").val();
    var tempStr = gradeList.join();
    gradeList = tempStr.split(",");


    var datefrom = "";
    var dateto = "";

    if (filterDatetype == 'time_selected') {

      datefrom = $('.datepickerFrom').val();
      dateto = $('.datepickerTo').val();

    } else {

      selected_term_to = $('#term-select_to').val();
      selected_term_from = $('#term-select_from').val();

      seleted_year_to = $('#select_years_to').val();
      seleted_year_from = $('#select_years_from').val();


      dateto = selected_term_from + "|" + seleted_year_from;
      datefrom = selected_term_to + "|" + seleted_year_to;

      //    console.log("to");
      //    console.log(selected_term_to);
      //    console.log(seleted_year_to);
      //    console.log("from");
      //    console.log(selected_term_from);
      //    console.log(seleted_year_from);

    }



    // var datefrom = $('.datepickerFrom').val();
    // var dateto = $('.datepickerTo').val();
    var title = gradeList + "  (" + datefrom + ")-(" + dateto + ")";
    console.log(title);

    var data2 = JSON.stringify({
      "branches": branchList,
      "grades": gradeList,
      "filtertype": "Branch",
      "datefrom": datefrom,
      "dateto": dateto,
      flag: 1
    });
    console.log(data2)
    var dummyData = JSON.stringify({
      "branches": branchList,
      "grades": ["G09"],
      "datefrom": datefrom,
      "dateto": dateto,
      "flag": 2,
      "filtertype": filtertype
    });
    // alert(dummyData+ "dummydata")
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/EnrollmentGraph", 'application/json', dummyData, function (response) {
      console.log("dates response" + response);
      $('#data').text("");

      $('#heading').text("Latest Available Data:");
      $.each(response, function (i, response) {
        $('#data').append(i + ': ' + response + '<br>')
      });
    });
    console.log(data2)
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/EnrollmentGraph", 'application/json', data2, function (response) {
      // console.log(grades);
      var oderedList = ['New Learners at new school','Kickout', 'Total Returning', 'New Learners at existing school'];

      for (var reason in oderedList) {
        var y = 0;
        var graphData = {
          name,
          x: [],
          y: [],
          type: 'bar'
        };

        graphData['name'] = oderedList[reason];
        for (var branch in response[oderedList[reason]]) {
          graphData['x'].push("All branches");
          y += response[oderedList[reason]][branch];
          //  text += response[reason][branch];
        }
        //graphData['text']=y;
        graphData['y'].push(y);
        tempLis2.push(graphData);

      }
      barLayout = {
        barmode: 'stack',

        yaxis: {
          title: 'Number of students'
        },
        showlegend: false
      };
      document.getElementById("progress_container").style.display = 'none';
      Plotly.newPlot(barGraphDivAll, tempLis2, barLayout, config);
    });






    var data = JSON.stringify({
      "branches": branchList,
      "grades": gradeList,
      "filtertype": filtertype,
      "datefrom": datefrom,
      "dateto": dateto,
      "flag": 1
    });
    console.log(data);
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/EnrollmentGraph", 'application/json', data, function (response) {
      console.log(response);
      var orderedList = ['New Learners at new school','Kickout', 'Total Returning', 'New Learners at existing school'];

      for (var reason in orderedList) {
        var graphData = {
          name,
          x: [],
          y: [],
          type: 'bar'
        };
        // graphData['name'] = reason;

        graphData['name'] = orderedList[reason];
        console.log(orderedList[reason])
        for (var branch in response[orderedList[reason]]) {
          graphData['x'].push(branch);
          graphData['y'].push(response[orderedList[reason]][branch]);

          // graphData['text'].push(response[reason][branch]);
        }
        tempLis.push(graphData);
        console.log(graphData)
      }
      barLayout2 = {
        barmode: 'stack',
        title: title,
        yaxis: {
          title: 'Number of students'
        }
      };

      Plotly.newPlot(barGraphDiv, tempLis, barLayout2, config);
    });

  });
  // console.log(data);


  //resize trigger
  $(window).resize(function () {
    if (this.resizeTO) clearTimeout(this.resizeTO);
    this.resizeTO = setTimeout(function () {
      $(this).trigger('resizeEnd');
    }, 500);
  });

  //redraw graph when window resize is completed  
  $(window).on('resizeEnd', function () {
    Plotly.newPlot(barGraphDiv, tempLis, barLayout2, config);
    Plotly.newPlot(barGraphDivAll, tempLis2, barLayout, config);

  });
  $('input:radio[name="group1"]').change(function () {
    if ($(this).val() == 'Branch') {
      $('#branches-select').attr('disabled', false);
      $('#branches-select').material_select();
      $('#schools-select').attr('disabled', true);
    } else if ($(this).val() == 'School') {
      $('#schools-select').attr('disabled', false);
      $('#schools-select').material_select();
      $('#branches-select').attr('disabled', true);
    }
  });



  $("input[name$='time_selection']").click(function () {
    var selected = $(this).val();
    console.log(selected);
    if (selected == 'time_term_year') {

      $('.datepickerFrom').attr('disabled', true);
      $('.datepickerTo').attr('disabled', true);

      $('#term-select_to').attr('disabled', false);
      $('#term-select_from').attr('disabled', false);
      $('#select_years_to').attr('disabled', false);
      $('#select_years_from').attr('disabled', false);
      $('select').material_select();

    } else if (selected == 'time_selected') {

      $('.datepickerFrom').attr('disabled', false);
      $('.datepickerTo').attr('disabled', false);


      $('#term-select_to').attr('disabled', true);
      $('#term-select_from').attr('disabled', true);
      $('#select_years_to').attr('disabled', true);
      $('#select_years_from').attr('disabled', true);
      $('select').material_select();



    }
  });


  //date picker
  $('.datepickerFrom').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    clear: 'Clear',
    format: 'yyyy-mm-dd',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
  });
  $('.datepickerTo').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    format: 'yyyy-mm-dd',
    clear: 'Clear',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
  });


});