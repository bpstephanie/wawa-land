/**const updatePostModal = new bootstrap.Modal(document.getElementById("updatePostModal"));
const editButtons = document.getElementsByClassName("btn-edit");
const updateConfirm = document.getElementById("updateConfirm");
*/

const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    updateConfirm.href = `edit_post/${postId}`;
    updatePostModal.show();
  });
}*/

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let postId = e.target.getAttribute("post_id");
      deleteConfirm.href = `delete_post/${postId}`;
      deletePostModal.show();
    });
  }
