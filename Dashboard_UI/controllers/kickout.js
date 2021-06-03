$(document).ready(function () {
  $("progress_container").hide();
  document.getElementById("progress_container").style.display = 'none';
  var $branches = $("#branches-select");
  var $schools = $("#schools-select");
  var $select_years_to = $('#select_years_to');
  var $select_years_from = $('#select_years_from');
  var graphDiv = document.getElementById("kickoutBar");
  var graphDivAll = document.getElementById("kickoutBarAll");
  //var colors = ['rgba(0,174,219,0.9)','rgba(162,0,255,0.9)','rgba(0,0,0,0.9)','rgba(212,18,67,0.9)','rgba(142,193,39,0.9)','rgba(96,35,32,0.9)','rgba(243,119,53,0.9)','rgba(209,17,65,0.9)','rgba(0,177,89,0.9)','rgba(55,56,84,0.9)','rgba(255, 51, 159 ,0.9)','rgba(245, 61, 61  ,0.9)','rgba(36, 113, 163,0.9)','rgba(125, 206, 160,0.9)','rgba(120, 40, 31  ,0.9)','rgba(156, 109, 50 ,0.9)','rgba(71, 156, 50,0.9)','rgba(156, 50, 82,0.9)','rgba(31, 255, 12,0.9)']
  //var colors = [ 'rgba(158, 27, 72, 0.9)', 'rgba(89, 23, 176, 0.9)', 'rgba(86, 23, 148, 0.9)', 'rgba(62, 146, 2, 0.9)', 'rgba(7, 160, 163, 0.9)', 'rgba(146, 137, 24, 0.9)', 'rgba(111, 24, 170, 0.9)','rgba(0,174,219,0.9)','rgba(162,0,255,0.9)','rgba(0,0,0,0.9)','rgba(212,18,67,0.9)','rgba(96,35,32,0.9)','rgba(243,119,53,0.9)','rgba(209,17,65,0.9)','rgba(0,177,89,0.9)','rgba(55,56,84,0.9)','rgba(255, 51, 159 ,0.9)','rgba(245, 61, 61  ,0.9)','rgba(36, 113, 163,0.9)','rgba(125, 206, 160,0.9)','rgba(120, 40, 31  ,0.9)','rgba(156, 109, 50 ,0.9)','rgba(71, 156, 50,0.9)','rgba(156, 50, 82,0.9)','rgba(31, 255, 12,0.9)', 'rgba(157, 142, 12, 0.9)','rgba(151, 60, 110, 0.9)', 'rgba(173, 167, 15, 0.9)', 'rgba(71, 24, 135, 0.9)', 'rgba(155, 106, 42, 0.9)', 'rgba(33, 17, 132, 0.9)', 'rgba(163, 2, 88, 0.9)', 'rgba(25, 139, 83, 0.9)', 'rgba(118, 85, 31, 0.9)', 'rgba(156, 123, 29, 0.9)', 'rgba(146, 7, 120, 0.9)', 'rgba(100, 129, 36, 0.9)', 'rgba(144, 22, 128, 0.9)', 'rgba(18, 105, 154, 0.9)', 'rgba(64, 139, 14, 0.9)', 'rgba(59, 174, 4, 0.9)', 'rgba(138, 171, 9, 0.9)', 'rgba(20, 147, 32, 0.9)', 'rgba(95, 22, 150, 0.9)', 'rgba(121, 61, 40, 0.9)', 'rgba(30, 136, 78, 0.9)', 'rgba(62, 48, 152, 0.9)', 'rgba(92, 32, 150, 0.9)', 'rgba(44, 136, 134, 0.9)', 'rgba(62, 62, 143, 0.9)', 'rgba(126, 87, 31, 0.9)', 'rgba(146, 52, 60, 0.9)', 'rgba(32, 141, 15, 0.9)', 'rgba(6, 173, 103, 0.9)', 'rgba(114, 127, 36, 0.9)', 'rgba(34, 123, 21, 0.9)', 'rgba(142, 16, 116, 0.9)', 'rgba(55, 162, 47, 0.9)', 'rgba(83, 160, 11, 0.9)', 'rgba(2, 178, 138, 0.9)', 'rgba(132, 20, 125, 0.9)', 'rgba(168, 13, 77, 0.9)', 'rgba(18, 100, 128, 0.9)', 'rgba(80, 167, 33, 0.9)', 'rgba(36, 123, 38, 0.9)', 'rgba(44, 15, 165, 0.9)', 'rgba(66, 32, 175, 0.9)', 'rgba(120, 107, 25, 0.9)', 'rgba(24, 170, 44, 0.9)', 'rgba(163, 44, 26, 0.9)', 'rgba(134, 42, 101, 0.9)', 'rgba(37, 32, 133, 0.9)', 'rgba(22, 143, 10, 0.9)', 'rgba(77, 154, 40, 0.9)', 'rgba(38, 124, 155, 0.9)', 'rgba(92, 162, 16, 0.9)', 'rgba(7, 150, 132, 0.9)', 'rgba(140, 172, 0, 0.9)', 'rgba(24, 68, 121, 0.9)', 'rgba(150, 149, 12, 0.9)', 'rgba(86, 140, 36, 0.9)', 'rgba(43, 128, 142, 0.9)', 'rgba(7, 35, 167, 0.9)', 'rgba(61, 149, 136, 0.9)', 'rgba(153, 83, 38, 0.9)', 'rgba(130, 3, 147, 0.9)', 'rgba(145, 12, 29, 0.9)', 'rgba(98, 123, 37, 0.9)', 'rgba(54, 64, 142, 0.9)', 'rgba(136, 25, 125, 0.9)', 'rgba(163, 56, 30, 0.9)', 'rgba(3, 122, 162, 0.9)', 'rgba(46, 160, 36, 0.9)', 'rgba(8, 17, 160, 0.9)', 'rgba(179, 67, 16, 0.9)', 'rgba(136, 146, 42, 0.9)', 'rgba(133, 16, 144, 0.9)', 'rgba(14, 49, 170, 0.9)', 'rgba(42, 39, 162, 0.9)', 'rgba(179, 35, 112, 0.9)', 'rgba(32, 164, 74, 0.9)', 'rgba(150, 139, 47, 0.9)', 'rgba(63, 94, 148, 0.9)', 'rgba(112, 148, 6, 0.9)', 'rgba(4, 144, 152, 0.9)', 'rgba(57, 133, 142, 0.9)', 'rgba(78, 166, 29, 0.9)', 'rgba(107, 165, 15, 0.9)', 'rgba(54, 140, 69, 0.9)', 'rgba(23, 42, 176, 0.9)', 'rgba(153, 57, 76, 0.9)', 'rgba(58, 146, 62, 0.9)', 'rgba(132, 150, 50, 0.9)', 'rgba(70, 39, 124, 0.9)', 'rgba(173, 21, 79, 0.9)', 'rgba(7, 178, 45, 0.9)', 'rgba(141, 25, 158, 0.9)', 'rgba(121, 141, 33, 0.9)', 'rgba(115, 147, 40, 0.9)', 'rgba(34, 166, 136, 0.9)', 'rgba(49, 125, 144, 0.9)', 'rgba(99, 32, 143, 0.9)', 'rgba(48, 80, 160, 0.9)'];
  var config = {
    modeBarButtonsToRemove: ['autoScale2d', 'resetScale2d',
      'hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d'
    ],
    displaylogo: false
  };
  var allbranches = [];
  var allschools = [];
  var allyears = [];

  function ajaxCallsFunc(type, url, contentType, data, callback) {
    $.ajax({
      type: type,
      url: url,
      contentType: contentType,
      data: data,
      success: callback
    });
  }
  //var data = JSON.stringify({"BranchList":["Makhaza", "Ebony Park"],"filter_type":"Branch","date_from":"2015-12-04", "date_to":"2017-09-29"});
  // console.log(data);  
  ajaxCallsFunc('POST', "http://41.164.192.98:5000/Branches", 'application/json', null, function (branches) {
    console.log(branches);
    $.each(branches, function (i, branch) {
      $branches.append('<option value="' + branch + '">' + branch + '</option>');
      $branches.material_select();
      allbranches.push(branch);
    });
  });
  ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetSchools", 'application/json', null, function (schools) {
    console.log(schools);
    $.each(schools, function (i, school) {
      $schools.append('<option value="' + school + '">' + school + '</option>');
      $schools.material_select();
      allschools.push(school);
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
  var tempLis2 = [];
  var tempLis = [];
  $("#drawgraph").click(function () {

    document.getElementById("progress_container").style.display = 'block';
    //$("progress_container").show();
    tempLis2 = [];

    var filtertype = $('input[name=group1]:checked').val();
    var filterDatetype = $('input[name=time_selection]:checked').val();
    if (filtertype == "Branch") {
      var branchList = $("#branches-select").val();
      // console.log(branchList)
    } else if (filtertype == "allbranches") {
      filtertype = "Branch";
      var branchList = allbranches;
    } else if (filtertype == "School") {
      var branchList = $("#schools-select").val();
    } else if (filtertype == "allschools") {
      filtertype = "School";
      branchList = allschools;
      //alert(branchList);
    }


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
    var data2 = JSON.stringify({
      "branches": allbranches,
      "filtertype": "Branch",
      "datefrom": datefrom,
      "dateto": dateto,
      flag: 1
    });
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/KickoutGraph", 'application/json', data2, function (response) {

      console.log(response);
      var lis = [];

      for(var reason in response){
        for(var branch in response[reason]){
          if(lis.indexOf(branch) == -1){
            lis.push(branch);  
          }
        }
      }
      totalCount = lis.length;
      var i = 0;
      for (var reason in response) {
        var y = 0;
        var graphData = {
          name,
          x: [],
          y: [],
          type: 'bar',

        };
        graphData['name'] = reason;
        //   graphData['marker']['color'] = colors[i];
        for (var branch in response[reason]) {
          graphData['x'].push("All branches");
          y += response[reason][branch];
        }
       
        y = (y / totalCount);
       
        graphData['y'].push(y);
        tempLis2.push(graphData);
        i++;
      }

      Plotly.newPlot(graphDivAll, tempLis2, {
        showlegend: false,
        barmode: 'stack',
        yaxis: {
          title: '% of students',
          //   range: [0, 100]
        }
      }, config);
    });

    tempLis = [];
    var dummyData = JSON.stringify({
      "branches": branchList,
      "datefrom": datefrom,
      "dateto": dateto,
      "flag": 2,
      "filtertype": filtertype
    });


    ajaxCallsFunc('POST', "http://41.164.192.98:5000/KickoutGraph", 'application/json', dummyData, function (response) {
      console.log(response);
      $('#data').text("");

      $('#heading').text("Latest Available Data:");
      $.each(response, function (i, response) {
        $('#data').append(i + ': ' + response + '<br>');
      });
    });

    // alert(branchList, filtertype, datefrom, dateto);
    var title1 = "% of students (" + datefrom + ") - (" + dateto + ")";
    var data = JSON.stringify({
      "branches": branchList,
      "filtertype": filtertype,
      "datefrom": datefrom,
      "dateto": dateto,
      flag: 1
    });


    // console.log(data);

    ajaxCallsFunc('POST', "http://41.164.192.98:5000/KickoutGraph", 'application/json', data, function (response) {
      console.log(response);
      var i = 0;
      for (var reason in response) {

        var graphData = {
          name,
          x: [],
          y: [],
          type: 'bar',
          marker: {
            width: 1,


          }
        };
        graphData['name'] = reason;
        //  graphData['marker']['color'] = colors[i];
        for (var branch in response[reason]) {
          graphData['x'].push(branch);
          graphData['y'].push(response[reason][branch]);
        }
        tempLis.push(graphData);
        i++
      }
      console.log(tempLis);


      // var layout = ;
      document.getElementById("progress_container").style.display = 'none';

      Plotly.newPlot(graphDiv, tempLis, {
        barmode: 'stack',
        yaxis: {
          title: '% of students',
          range: [0, 100]
        },
        title: title1,
        titlefont: {
          size: 12

        }
      }, config);
    });
  });
  // resize trigger
  $(window).resize(function () {
    if (this.resizeTO) clearTimeout(this.resizeTO);
    this.resizeTO = setTimeout(function () {
      $(this).trigger('resizeEnd');
    }, 500);
  });

  // redraw graph when window resize is completed  
  $(window).on('resizeEnd', function () {
    //Plotly.newPlot(graphDiv, tempLis);
    Plotly.newPlot(graphDivAll, tempLis2, {
      showlegend: false,
      barmode: 'stack',

      yaxis: {
        title: '% of students',
        range: [0, 100]
      }
    }, config);
    Plotly.newPlot(graphDiv, tempLis, {
      barmode: 'stack',
      yaxis: {
        title: '% of students',
        range: [0, 100]
      },
      title: title1,
      titlefont: {
        size: 12
      }
    }, config);
  });

  //date picker
  $('.datepickerFrom').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15, // Creates a dropdown of 15 years to control year,
    today: 'Today',
    format: 'yyyy-mm-dd',
    clear: 'Clear',
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



////for selecting all branches 
// $('#branches-select').prev('ul[id^="select-options-"]').children('li:first').on('click', function () {
//   var selector = 'li.active';
//   if ($(this).hasClass('active')) {
//     selector = 'li:not(".active")';
//   }

//   $(this).siblings(selector).each(function () {
//     $(this).click();
//   });

//   $('span', this).contents().last()[0].textContent = $(this).text().trim() === 'Check All' ? 'Uncheck All' : 'Check All';
//   // Check values of selected options
//   console.log($(this).parent().next().val());
// });

////for selecting all schools   
// $schools.prev('ul[id^="select-options-"]').children('li:first').on('click', function () {
//     var selector = 'li.active';
//     if ($(this).hasClass('active')) {
//       selector = 'li:not(".active")';
//     }

//     $(this).siblings(selector).each(function () {
//       $(this).click();
//     });

//     $('span', this).contents().last()[0].textContent = $(this).text().trim() === 'Check All' ? 'Uncheck All' : 'Check All';
//     // Check values of selected options
//     console.log($(this).parent().next().val());
//   });