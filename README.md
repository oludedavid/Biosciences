# Biosciences
const currentDate = new Date();
const dayNames = ["Sun", "Mon", "Tue", "Wed", "Thurs", "Fri", "Sat"];
const monthNames = [
  "Jan",
  "Feb",
  "Mar",
  "Apr",
  "May",
  "Jun",
  "Jul",
  "Aug",
  "Sep",
  "Oct",
  "Nov",
  "Dec"
];
const fullYear = currentDate.getFullYear();
const currentMonth = monthNames[currentDate.getMonth()];
const currentDayOfWeek = dayNames[currentDate.getDay()];
const currentDateOfTheMonth = currentDate.getDate();

let todaysDate;

if(currentDateOfTheMonth === 1 || 21 || 30){
    todaysDate= `Today's Date is ${currentDayOfWeek}, ${currentDateOfTheMonth}st of ${currentMonth} ${fullYear}`
}if (currentDateOfTheMonth === 2 || 22){
    todaysDate= `Today's Date is ${currentDayOfWeek}, ${currentDateOfTheMonth}nd of ${currentMonth} ${fullYear}`
} if (currentDateOfTheMonth === 3 || 23){
    todaysDate= `Today's Date is ${currentDayOfWeek}, ${currentDateOfTheMonth}rd of ${currentMonth} ${fullYear}`
}else{
    todaysDate= `Today's Date is ${currentDayOfWeek}, ${currentDateOfTheMonth}th of ${currentMonth} ${fullYear}` 
}

console.log(todaysDate)

//The navigation bar component
function Navbar() {
  return (
    <nav className="navbar">
      <img src="./images/sticky-note.png" className="nav-img" />
      <h1 className="nav-logo">TodoApp.js</h1>
    </nav>
  );
}

//todo component

function ToDo(props) {
  return (
    <section className="todo">
      <input type="checkbox" className="todo-checkbox" />
      <h2>{props.text}</h2>
      <p>{props.date}</p>
      <div className="btn-container">
        <button className="delete-btn btn">
          <img src="./images/delete.png" className="delete icon" />
        </button>
        <button className="edit-btn btn">
          <img src="./images/edit.png" className="edit icon" />
        </button>
      </div>
    </section>
  );
}


//form component
function Form() {
   
  const [inputText, setInputText] = React.useState(["I am going home"]);
  const [inputDate, setInputDate] = React.useState(["20/3/1995"]);
  const [todo, setToDo] = React.useState(false);


  //change handler for text
  function handleTextChange(event){
    let textValue = event.target.value
   setInputText((preText)=>[...preText, textValue])
}

//change handler for date
function handleDateChange(event){
    let dateValue = event.target.value
    setInputDate((preDate)=>[...preDate, dateValue])
}

 //click handler CREATE Button
 function clickHandler(){
     {setToDo((prevState)=> !prevState)}
    <ToDo text={inputText} date={inputDate}/>
  }


  return (
    <section className="form">
      <div className="form-container">
        <div>
          <input
            type="text"
            value={inputText}
            placeholder="your objective"
            className="form-text form-input"
          />
        </div>
        <div>
          <input type="date" className="form-date form-input" value={inputDate} />
        </div>
        <div>
          <button className="form-input">Add to objectives</button>
        </div>
      </div>

      <h1>Objective Items</h1>

      {todo && <ToDo/>}
    </section>
  );
}

//The main container that holds the todo items component
function Main() {
  return (
    <main className="main-todo-container">
      <Form />
    </main>
  );
}

//The footer
function Footer() {
  return (
    <footer className="footer">
      <p>Dave.io &copy;</p>
    </footer>
  );
}

//The source of truth of the react application
function App() {
  return (
    <div className="main-cont">
      <Navbar />
      <Main />
      <Footer />
    </div>
  );
}

//Using react.render to render the jsx in the root html element
ReactDOM.render(<App />, document.getElementById("root"));
