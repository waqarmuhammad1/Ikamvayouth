$(document).ready(function () {
  $("progress_container").hide();
  document.getElementById("progress_container").style.display = 'none';
  var $branches = $("#branches-select");
  var $schools = $("#schools-select");
  var $select_years_to = $('#select_years_to');
  var $select_years_from = $('#select_years_from');
  var barGraphDiv = document.getElementById("tutorsBar");
  var barGraphDiv2 = document.getElementById("tutorsBar2");
  var allyears = [];
  var allbranches = [];
  var config = {
    modeBarButtonsToRemove: ['autoScale2d', 'resetScale2d',
      'hoverClosestCartesian', 'hoverCompareCartesian', 'zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d'
    ],
    displaylogo: false
  };

  var barLayout;

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
    console.log(branches);
    $.each(branches, function (i, branch) {
      $branches.append('<option value="' + branch + '">' + branch + '</option>');
      $branches.material_select();
      allbranches.push(branch);
    });
  });


  ajaxCallsFunc('POST', "http://41.164.192.98:5000/GetSchools", 'application/json', null, function (schools) {
    //  console.log(schools);
    $.each(schools, function (i, school) {
      $schools.append('<option value="' + school + '">' + school + '</option>');
      $schools.material_select();
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


  var finalData = [];
  var finalData1 = [];

  $("#drawgraph").click(function () {
    finalData = [];
    finalData1 = [];
    document.getElementById("progress_container").style.display = 'block';


    var filtertype = $('input[name=group1]:checked').val();
    var filterDatetype = $('input[name=time_selection]:checked').val();
    if (filtertype == "Branch") {
      var branchList = $("#branches-select").val();
    } else if (filtertype == "allbranches") {
      filtertype = "Branch";
      var branchList = allbranches;

    }

    var schedule = $("#schedule").val();
    schedule = schedule.join();
    var flag = parseInt($("#flag").val());
    var flagtext;


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


    }

    //var datefrom = $('.datepickerFrom').val();
    //var dateto = $('.datepickerTo').val();
    console.log(filtertype, branchList, flag, datefrom, dateto);
    var title1 = " (" + datefrom + ") - (" + dateto + ")";

    var dummyData = JSON.stringify({

      "instituteList": branchList,
      "datefrom": datefrom,
      "dateto": dateto,
      "flag": 4,
      "weekDay": schedule,
      "filtertype": filtertype
    });
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/TutorGraph", 'application/json', dummyData, function (response) {
      console.log(response);
      $('#data').text("");

      $('#heading').text("Latest Available Data (students):");
      $.each(response, function (i, response) {
        $('#data').append(i + ': ' + response + '<br>')
      });
    });
    var dummyData2 = JSON.stringify({
      "instituteList": branchList,
      "datefrom": datefrom,
      "dateto": dateto,
      "flag": 5,
      "weekDay": schedule,
      "filtertype": filtertype
    });
    ajaxCallsFunc('POST', "http://41.164.192.98:5000/TutorGraph", 'application/json', dummyData2, function (response) {
      console.log(response);
      $('#data2').text("");
      $('#heading2').text("Latest Available Data (staff):");
      $.each(response, function (i, response) {
        $('#data2').append(i + ': ' + response + '<br>')
      });
    });

    if (flag == 1 || flag == 2) {
      finalData = [];
      finalData1 = [];
      if (flag == 1) {
        flagtext = "Number of pupils per tutor";
      } else if (flag == 2) {
        flagtext = "% active tutors";
      }
      var data = JSON.stringify({
        "instituteList": allbranches,
        "filtertype": filtertype,
        "flag": flag,
        "weekDay": schedule,
        "datefrom": datefrom,
        "dateto": dateto
      });

      ajaxCallsFunc('POST', "http://41.164.192.98:5000/TutorGraph", 'application/json', data, function (response) {
        console.log("this"+response);
        var graphData = {
          type: "bar",
          x: [],
          y: [],
          text: '',
          textposition: 'auto',
          hoverinfo: 'none'
        };
        var a = 0;
        for (var branch in response) {
          graphData['x'].push("All branches");
          a += response[branch];
        }
        k = a / 17;
       // console.log(k);
        k = k.toFixed(2);

        graphData['text'] = k;
        graphData['y'].push(k);

        finalData1.push(graphData);
        document.getElementById("progress_container").style.display = 'none';
        if (flag == 2) {
          Plotly.newPlot(barGraphDiv2, finalData1, {
            yaxis: {
              title: flagtext,
              range: [0, 100]
            },
            bargap: 0.5
          }, config);
        } else if (flag == 1) {
          Plotly.newPlot(barGraphDiv2, finalData1, {
            yaxis: {
              title: flagtext
            },
            bargap: 0.5

          }, config);
        }
      });



      var data = JSON.stringify({
        "instituteList": branchList,
        "filtertype": filtertype,
        "flag": flag,
        "weekDay": schedule,
        "datefrom": datefrom,
        "dateto": dateto
      });

      ajaxCallsFunc('POST', "http://41.164.192.98:5000/TutorGraph", 'application/json', data, function (response) {
        console.log(response);
        var graphData = {
          type: "bar",
          x: [],
          y: [],
          text: [],
          textposition: 'auto',
          hoverinfo: 'none'
        };
        for (var branch in response) {
          graphData['x'].push(branch);
          graphData['y'].push(response[branch]);
          graphData['text'].push(response[branch]);

        }
        finalData.push(graphData);
        document.getElementById("progress_container").style.display = 'none';

        if (flag == 1) {
          Plotly.newPlot(barGraphDiv, finalData, {
            yaxis: {
              title: flagtext
            },
            title: flagtext + title1,
            titlefont: {
              size: 12

            }

          }, config);
        } else if (flag == 2) {

          Plotly.newPlot(barGraphDiv, finalData, {
            yaxis: {
              title: flagtext,
              range: [0, 100]
            },
            title: flagtext + title1,
            titlefont: {
              size: 12

            }

          }, config);
        }
      });
    } else if (flag == 3) {
      finalData = [];
      finalData1 = [];
      flagtext = "Number of pupils per tutor";
      var errorData = JSON.stringify({
        "instituteList": allbranches,
        "filtertype": "Branch",
        "flag": 3,
        "weekDay": schedule,
        "datefrom": datefrom,
        "dateto": dateto
      });
      ajaxCallsFunc('POST', "http://41.164.192.98:5000/TutorGraph", 'application/json', errorData, function (response) {
       // alert("this"+response);
        var minList = [];
        var maxList = [];
     
        var temp = {
          x: [],
          y: [],
          type: 'scatter'
        };
        console.log(response);
        for (var branch in response) {
          temp['x'].push("All branches");
          minList.push(parseInt(response[branch][0]));
          maxList.push(parseInt(response[branch][1]));
        }
        
        var min = Math.min.apply(null,minList);
        var max = Math.max.apply(null, maxList);
        // console.log(Math.min(maxList));
        temp['y'].push(min);
        temp['y'].push(max);

        //finalData1 = temp;
        finalData1.push(temp);
        Plotly.newPlot(barGraphDiv2, finalData1, {
          yaxis: {
            title: flagtext
          },
          showlegend: false,
          hovermode: 'closest',
        }, config);
      });
      //error bar chart
      var errorData = JSON.stringify({
        "instituteList": branchList,
        "filtertype": filtertype,
        "flag": 3,
        "weekDay": schedule,
        "datefrom": datefrom,
        "dateto": dateto
      });
      ajaxCallsFunc('POST', "http://41.164.192.98:5000/TutorGraph", 'application/json', errorData, function (response) {
        
        console.log(response);
        
        for (var branch in response) {
          var temp = {
            x: [],
            y: [],
            type: 'scatter'
          };
          temp['x'].push(branch);
          temp['x'].push(branch);
          temp['y'].push(response[branch][0]);
          temp['y'].push(response[branch][1]);
          finalData.push(temp);
        }
        document.getElementById("progress_container").style.display = 'none';

        Plotly.newPlot(barGraphDiv, finalData, {
          yaxis: {
            title: flagtext
          },
          showlegend: false,
          hovermode: 'closest',
          title: flagtext + title1,
          titlefont: {
            size: 12
          }
        }, config);
      });
    }
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
  // resize trigger
  $(window).resize(function () {
    if (this.resizeTO) clearTimeout(this.resizeTO);
    this.resizeTO = setTimeout(function () {
      $(this).trigger('resizeEnd');
    }, 500);
  });

  // redraw graph when window resize is completed  
  $(window).on('resizeEnd', function () {
    Plotly.newPlot(barGraphDiv, finalData, {
      yaxis: {
        title: flagtext
      },
      showlegend: false,
      hovermode: 'closest',
    }, config);
    Plotly.newPlot(barGraphDiv2, finalData1, {
      yaxis: {
        title: flagtext
      },
      showlegend: false,
      hovermode: 'closest',

    }, config);


    // Plotly.newPlot(barErrorGraphDiv, barGraphData);

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
    clear: 'Clear',
    format: 'yyyy-mm-dd',
    close: 'Ok',
    closeOnSelect: false // Close upon selecting a date,
  });


  $('select').material_select();
});