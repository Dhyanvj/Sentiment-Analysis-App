$(document).ready(function() {
    $("#analyze-button").click(function() {
        let text = $("#text-input").val();

        $.ajax({
            type: "POST",
            url: "/analyze",
            data: { text: text },
            success: function(response) {
                $("#result").text("Sentiment: " + response.sentiment);
            },
            error: function() {
                $("#result").text("Error analyzing sentiment.");
            }
        });
    });
});
