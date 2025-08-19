// Elements
const totalPrice = document.getElementById('id_totallPrice');

const loanValue = document.getElementById('id_loanAmount');
const tenureValue = document.getElementById('tenureDropdown');

const interestRange = document.getElementById('interestRange');
const interestValue = document.getElementById('interestValue');

const downpaymentRange = document.getElementById('downpaymentRange');
const downpaymentValue = document.getElementById('downpaymentValue');

// Display slider value
function sliderValue(inputRange, inputValue, type = 'int') {
    if (type === 'float') {
        inputValue.textContent = parseFloat(inputRange.value).toFixed(1) + " %";
        inputRange.addEventListener('input', function () {
            inputValue.textContent = parseFloat(this.value).toFixed(1) + " %";
        });
    } else {
        inputValue.textContent = parseInt(inputRange.value, 10);
        inputRange.addEventListener('input', function () {
            inputValue.textContent = parseInt(this.value, 10);
        });
    }
}

// Interest rate background update
function updateSliderRate(inputRange) {
    const min = inputRange.min || 0;
    const max = inputRange.max || 100;
    const value = inputRange.value;

    const percent = ((value - min) / (max - min)) * 100;
    inputRange.style.background = `linear-gradient(to right, teal ${percent}%, #ddd ${percent}%)`;
}

// Down payment background update
function updateSliderLoan(inputRange) {
    const min = inputRange.min || 0;
    const max = inputRange.max || 100;
    const value = inputRange.value;

    const percent = ((value - min) / (max - min)) * 100;
    inputRange.style.background = `linear-gradient(to right, teal ${percent}%, #ddd ${percent}%)`;
}


function getEmiValue() {

    let formData = $("#emiForm").serialize();

    $.ajax({
        url: "../SubmitEmi/",
        type: "POST",
        data: formData,
        success: function (response) {
            $("#loader-img").hide();
            if (response.success) {
                $("#emiResult").text("₹" + response.resultData);
            } else {
                $("#emiResult").text("Error: " + response.error);
            }
        },
        error: function () {
            $("#loader-img").hide();
            $("#emiResult-label").text("Something went wrong!");
        }
    });
}

function getGetLoanAmount(TotalPrice) {
    var LoanAmount = 0;
    var downAmount = $("#downpaymentRange").val();
    LoanAmount = TotalPrice - downAmount;
    return LoanAmount;
}

downpaymentRange.addEventListener('change', function () {

    updateSliderLoan(downpaymentRange);
    var LoanAmount = getGetLoanAmount($("#id_totallPrice").val());
    $("#id_loanAmount").val(LoanAmount).trigger("input").trigger("change");
    if (LoanAmount > 0) {
        $("#loader-img").show();
        setTimeout(function () {
            getEmiValue();
        }, 3000);
    }

});

interestRange.addEventListener('change', function () {
    if ($("#id_loanAmount").val() > 0) {
        updateSliderRate(interestRange);
        $("#loader-img").show();
        setTimeout(function () {
            getEmiValue();
        }, 3000);
    }
});

totalPrice.addEventListener('blur', function () {
    $('#downpaymentRange').prop('disabled', true);
    var CurrentTotalPrice = Number($("#id_totallPrice").val());
    var downpayvalue = Number($("#downpaymentRange").val()) - 1000;
    if (downpayvalue > CurrentTotalPrice) {
        console.log('CurrentTotalPrice:' + CurrentTotalPrice);
        console.log('downpayvalue:' + downpayvalue);
        $("#downpaymentRange").val(0).trigger("input").trigger("change");
        $("#downpaymentValue").text("0");
        $("#downpaymentRange").css("background", `linear-gradient(to right, teal 0%, rgb(221, 221, 221) 0%)`);
    }
    $("#loader-img").show();
    setTimeout(function () {
        var LoanAmount = getGetLoanAmount(CurrentTotalPrice);
        $("#id_loanAmount").val(LoanAmount).trigger("input").trigger("change");
        loanmaxmin(CurrentTotalPrice);
        setTimeout(function () {
            getEmiValue();
        }, 3000);
    }, 3000);

});

// loanValue.addEventListener('blur', function () {
//     totalLoan = $("#id_loanAmount").val();
//     if (totalLoan > 0) {
//         $("#loader-img").show();
//         setTimeout(function () {
//             getEmiValue();
//         }, 3000);
//     }
// });

tenureValue.addEventListener('change', function () {
    if ($("#id_loanAmount").val() > 0) {
        updateSliderRate(interestRange);
        $("#loader-img").show();
        setTimeout(function () {
            getEmiValue();
        }, 3000);
    }
});

function loanmaxmin(totalLoan) {
    totalLoan = totalLoan - 1000;
    console.log('totalLoan:' + totalLoan);
    $('#downpaymentRange').attr('max', totalLoan);
    setps = totalLoan / 1000;
    $('#downpaymentRange').attr('step', parseInt(setps));
    $('#downpaymentRange').prop('disabled', false);
    updateSliderLoan(downpaymentRange);
}

// Initial load
sliderValue(downpaymentRange, downpaymentValue);
sliderValue(interestRange, interestValue, 'float');
updateSliderLoan(downpaymentRange);
updateSliderRate(interestRange);