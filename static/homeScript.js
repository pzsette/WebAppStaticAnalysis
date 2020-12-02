$(document).ready(function() {

    function performOperation() {
        console.log("Done!");
    }

    $('#deposit').click(function () {
        let deposit_amount = document.getElementById("value").value;
        let actual_amount = document.getElementById("value").value;

        if (x.length != 0) {
            $.ajax({
                type: "POST",
                url: $SCRIPT_ROOT+"/deposit/"+deposit_amount+"/"+actual_amount,
                data: "{}",
                success: function() {
                    console.log("Deposit: "+x);
                }
            });
            //document.getElementById("amount").innerHTML =amoun;

        } else {
            alert("Insert integer value");
        }
    });

    $('#withdraw').click(function () {
        let withdraw_amount = document.getElementById("value").value;
        let actual_amount = document.getElementById("value").value;
        let x = (document.getElementById("value")).value;
        if (x.length != 0) {
            $.ajax({
                type: "POST",
                url: $SCRIPT_ROOT+"/withdraw/"+deposit_amount+"/"+actual_amount,
                data: "{}",
                success: function() {
                    console.log("Withdraw: "+x);
                }
            });
            //document.getElementById("amount").innerHTML = {{amount}};

        } else {
            alert("Insert integer value");
        }
    });

});