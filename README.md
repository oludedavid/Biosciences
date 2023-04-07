# Biosciences

body {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Poppins", sans-serif;
}
.main-cont {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding-top: 10px;
  gap: 100px;
}
.navbar {
  background: linear-gradient(
    90deg,
    rgba(253, 244, 245, 1) 0%,
    rgba(232, 160, 191, 1) 35%,
    rgba(192, 219, 234, 1) 80%
  );
  box-shadow: rgba(149, 157, 165, 0.2) 0px 8px 24px;
  border-radius: 5px;
  width: 90vw;
  height: 50px;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 10px;
}

.nav-img {
  width: 40px;
  height: 40px;
}

.nav-logo {
  font-weight: 400;
  font-size: 30px;
  padding-left: 10px;
  letter-spacing: 5px;
  line-height: 2px;
}

.main-todo-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.form-container{
  display: flex;
  gap: 20px;
  padding: 10px;
}

.form-input{
  height: 30px;
  width: 160px;
}
.form-container button{
  display: block;
  font-size: 15px;
  font-weight: 300;
  cursor: pointer;
  background-color: rgba(232, 160, 191, 1);
  border: 0;
  border-radius: 3px;
  filter: brightness(50%);
  color: white;
  padding: 5px;
}

.form-container button:hover{
  background-color: transparent;
  border: 0.2px solid;
  filter: brightness(0);
}

.form-date{
  padding: 5px;
}

.form-text{
  padding: 5px;
}

.todo{
  display: flex;
  padding: 20px;
  gap: 15px;
}

.todo p{
  padding: 12px;
}

.btn-container{
  padding: 20px;
  display: none;
}

.btn{
 height: 25px;
 width: 35px;
background-color: transparent;
border: 0 ;
cursor: pointer;
}

.delete-btn{
  margin-right: 2px;
}

.btn .icon{
  width: 100%;
  height: 100%;
}

.todo-checkbox:checked ~ .btn-container{
  display: block;
}

footer {
  width: 100vw;
  height: 50px;
  background-color: #c0dbea;
  text-align: center;
  position: absolute;
  bottom: 0;
}
