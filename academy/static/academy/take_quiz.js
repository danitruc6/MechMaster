document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('quiz-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the form from submitting normally

        const questions = document.querySelectorAll('.question');
        let score = 0;

        questions.forEach(question => {
            const selectedOption = question.querySelector('input[type="radio"]:checked');
            if (selectedOption) {
                const isCorrect = selectedOption.getAttribute('data-is-correct') === 'true';
                if (isCorrect) {
                    score++;
                }
            }
        });

        const scoreField = document.getElementById('score');
        scoreField.textContent = `Score: ${score}`;

        // Send the score to the server using AJAX
        const quizId = form.getAttribute('data-quiz-id');
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        fetch(`/submit_quiz/${quizId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
            },
            body: JSON.stringify({ score: score }),
        })
        .then(response => response.json())
        .then(data => {
            // Redirect to the quiz result page
            window.location.href = data.redirect_url;
        })
        .catch(error => {
            console.error('Error submitting quiz:', error);
        });
    });
});
