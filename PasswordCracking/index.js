import { initializeApp } from "https://www.gstatic.com/firebasejs/10.7.1/firebase-app.js";
import {
  collection,
  getFirestore,
  where,
  query,
  getDocs,
} from "https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore.js";
const firebaseConfig = {
  apiKey: "AIzaSyCoeusnxrCqvydla8X6_2b6UuCSjh-UnCQ",
  authDomain: "act-crypto.firebaseapp.com",
  projectId: "act-crypto",
  storageBucket: "act-crypto.appspot.com",
  messagingSenderId: "980194197032",
  appId: "1:980194197032:web:5080fcfdb12efd89bcbf1d",
  measurementId: "G-G38BPLRQCW",
};
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);


const loginBtn = document.getElementById("login-btn")

loginBtn.addEventListener("click", async()=>{
try{
    const snapshot = await getDocs(query(collection(db, "users",),where("password", "==", document.getElementById("password-input").value)))
    if(snapshot.docs.length == 1){
      window.location.href = "http://127.0.0.1:5500/Cryptography/landing-page.html";
    }
    else{
      alert("Login credentials are incorrect!")
    }
}catch(err){
    console.log(err)
}
})

