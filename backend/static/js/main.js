function toggleMobileSidebar() {
            const sidebar = document.getElementById('mobile-sidebar');
            sidebar.style.display = sidebar.style.display === 'none' ? 'block' : 'none';
}

document.addEventListener('DOMContentLoaded', function() {
            const addButton = document.querySelector('button.bg-green-600');
            const modal = document.getElementById('challengeModal');
            const cancelButton = modal.querySelector('button.bg-gray-700');
            
            addButton.addEventListener('click', function() {
                modal.classList.remove('hidden');
            });
            
            cancelButton.addEventListener('click', function() {
                modal.classList.add('hidden');
            });
});

