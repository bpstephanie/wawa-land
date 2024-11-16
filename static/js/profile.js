document.addEventListener('DOMContentLoaded', function() {
    const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");

    console.log("1");

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let postId = e.target.getAttribute("post_id");
            deleteConfirm.href = `delete_post/${postId}`;
            deletePostModal.show();
        });
    }

    console.log("1");

    const postTitleElements = document.querySelectorAll('[data-bs-toggle="modal"]');

    postTitleElements.forEach(function(titleElement) {
        titleElement.addEventListener('click', function() {
            var postId = this.getAttribute('data-bs-target').replace('#postModal', '');
            var postTitle = document.querySelector('#postModalLabel' + postId).textContent;
            var postContentElement = document.querySelector('#postModal' + postId + ' .modal-body p');
            var postContent = postContentElement.textContent;

            // Check if content is JSON and parse it
            try {
                var parsedContent = JSON.parse(postContent);
                postContentElement.innerHTML = Array.isArray(parsedContent) ? parsedContent.join('') : parsedContent;
            } catch (e) {
                // If not JSON, display the content as-is
                postContentElement.innerHTML = postContent;
            }

            // Populate the modal with the clicked post's title and content
            document.getElementById('postModalLabel' + postId).textContent = postTitle;
        });
    });
});
