let createNoteForm = document.forms['createNoteForm']
let title = document.getElementById('title');
let description = document.getElementById('description')
let submitBtn = document.getElementById('submitButton');
let updateBtn = document.querySelectorAll('.update-btn');
let currentNote = document.querySelectorAll('.currentNote');
let noteTitle = document.querySelectorAll('.noteTitle');
let noteDescription = document.querySelectorAll('.noteDescription');

createNoteForm.addEventListener("input", () => {
    if (title.value.trim() && description.value.trim()) {
        submitBtn.removeAttribute("disabled");
    } else {
        submitBtn.setAttribute("disabled", "disabled");
    }
});

for (let i = 0; i< updateBtn.length; i++) {
    updateBtn[i].addEventListener("click", () => {
        title.value = noteTitle[i].innerText
        description.value = noteDescription[i].innerText
        submitBtn.innerText = 'Update'
        currentNote[i].style.display = 'none'
        console.log(noteDescription.innerText)
    })
}

description.addEventListener('keyup', (e)=>{
    description.style.height = `auto`
    description.style.height = `${e.target.scrollHeight}px`
})
// updateBtn.forEach(item => {
//     item.addEventListener("click", () => {
//         title.value = noteTitle.innerText
//         description.value = noteDescription.innerText
//         item.innerText = 'Update'
//         currentNote.style.display = 'none'
//         console.log(noteDescription.innerText)
//     })
// });