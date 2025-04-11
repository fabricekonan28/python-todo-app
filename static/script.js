document.addEventListener('DOMContentLoaded', () => {
    const taskListDiv = document.getElementById('task-list');
    const addTaskForm = document.getElementById('add-task-form');

    // Fonction pour récupérer et afficher les tâches
    const fetchTasks = async () => {
        try {
            const response = await fetch('/tasks');
            const tasks = await response.json();
            taskListDiv.innerHTML = ''; // Efface la liste actuelle
            tasks.forEach(task => {
                const taskItem = document.createElement('div');
                taskItem.classList.add('task-item');
                taskItem.innerHTML = `
                    <span><strong>${task.title}</strong></span>
                    ${task.description ? `<span>${task.description}</span>` : ''}
                `;
                taskListDiv.appendChild(taskItem);
            });
        } catch (error) {
            console.error('Erreur lors de la récupération des tâches:', error);
            taskListDiv.innerHTML = '<p>Erreur lors du chargement des tâches.</p>';
        }
    };

    // Fonction pour ajouter une nouvelle tâche
    addTaskForm.addEventListener('submit', async (event) => {
        event.preventDefault();
        const titleInput = document.getElementById('title');
        const descriptionInput = document.getElementById('description');
        const title = titleInput.value;
        const description = descriptionInput.value;

        try {
            const response = await fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title, description }),
            });

            // ... (gestion de la réponse)

        } catch (error) {
            console.error('Erreur lors de l\'envoi de la requête:', error);
            alert('Erreur réseau lors de l\'ajout de la tâche.');
        }
    });

    // Charge les tâches au chargement de la page
    fetchTasks();
});