async function upload(){

let file = document.getElementById("fileUpload").files[0]

let formData = new FormData()

formData.append("file",file)

let response = await fetch("http://127.0.0.1:8000/analyze",{
method:"POST",
body:formData
})

let data = await response.json()

document.getElementById("result").innerHTML =
`
Company: ${data.company} <br>
Score: ${data.score} <br>
Decision: ${data.decision} <br>
Loan: ${data.loan}
`
}
