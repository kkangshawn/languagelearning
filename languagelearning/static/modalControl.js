const modifyWordModal = document.getElementById('modifyWordModalToggle')
modifyWordModal.addEventListener('show.bs.modal', event => {
  const button = event.relatedTarget
  const id = button.getAttribute('data-bs-id')
  const word = button.getAttribute('data-bs-word')
  const meaning = button.getAttribute('data-bs-meaning')
  const level = button.getAttribute('data-bs-level')

  const modalBodyInputWord = modifyWordModal.querySelector('.modal-body input#modifyWord')
  modalBodyInputWord.value = word
  const modalBodyInputMeaning = modifyWordModal.querySelector('.modal-body input#modifyMeaning')
  modalBodyInputMeaning.value = meaning
  const modalBodyInputLevel = modifyWordModal.querySelector(`.modal-body input#listGroupCheckableRadios${level}`)
  modalBodyInputLevel.checked = true
  document.getElementById('modifyForm').action = `${id}/modify`
})
const deleteWordModal = document.getElementById('deleteWordModalToggle')
deleteWordModal.addEventListener('show.bs.modal', event => {
  const button = event.relatedTarget
  const id = button.getAttribute('data-bs-id')
  const word = button.getAttribute('data-bs-word')
  const modalBody = deleteWordModal.querySelector('.modal-body')
  modalBody.innerHTML = `Are you sure to delete <strong><i>${word}</i></strong> ?`
  document.getElementById('deleteForm').action = `${id}/delete`
})

$(document).on('click', '.flip-card .flip-card-inner', function() {
    $(this).closest('.flip-card').toggleClass('flip')
    $(this).css('transform, rotateY(180deg)')
})