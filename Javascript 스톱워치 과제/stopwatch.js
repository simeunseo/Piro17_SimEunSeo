let millisecond = 0;
let second = 0;
const startBtn = document.querySelector(".start-btn");
const stopBtn = document.querySelector(".stop-btn");
const resetBtn = document.querySelector(".reset-btn");
const lapseMillisecond = document.querySelector(".time .millisecond");
const lapseSecond = document.querySelector(".time .second");
const record = document.querySelector(".record ul");
let intervalID;
let newRecord;
const selectAllBtn = document.querySelector(".select-all");
let selectOneBtn = document.querySelectorAll(".select");
let recordAll;
let newSelect;

startBtn.addEventListener("click", function () {
  clearInterval(intervalID);
  intervalID = setInterval(function () {
    millisecond++;
    if (millisecond > 99) {
      second++;
      millisecond = 0;
    }
    lapseMillisecond.innerText = String(millisecond).padStart(2, "0");
    lapseSecond.innerText = String(second).padStart(2, "0");
  }, 10);
});

stopBtn.addEventListener("click", function () {
  clearInterval(intervalID);
  newRecord = document.createElement("li");
  newRecord.innerHTML = `
    <button class="select">
        <input type="checkbox" class="check" />
    </button>
    <div class="record-time">
        <div class="second">00</div>
        <div class="colon">:</div>
        <div class="millisecond">00</div>
    </div>
  `;
  record.appendChild(newRecord);
  newRecord.lastElementChild.lastElementChild.innerText =
    lapseMillisecond.innerText;
  newRecord.lastElementChild.firstElementChild.innerText =
    lapseSecond.innerText;

  /*
  selectOneBtn = document.querySelectorAll(".select");
  selectOneBtn.forEach((btn) => {
    btn.addEventListener("click", function () {
      if (btn.firstElementChild.style.display == "none") {
        btn.firstElementChild.style.display = "unset";
        btn.lastElementChild.style.display = "none";
      } else {
        btn.firstElementChild.style.display = "none";
        btn.lastElementChild.style.display = "unset";
      }
    });
  });
  */
});

resetBtn.addEventListener("click", function () {
  millisecond = 0;
  second = 0;
  lapseMillisecond.innerText = "00";
  lapseSecond.innerText = "00";
  clearInterval(intervalID);
});

/*
selectAllBtn.addEventListener("click", function () {
  if (selectAllBtn.firstElementChild.style.display == "none") {
    //이미 선택된 상태라면 선택해제한다
    selectAllBtn.firstElementChild.style.display = "unset";
    selectAllBtn.lastElementChild.style.display = "none";
    for (let i = 0; i < recordAll.length; i++) {
      recordAll.item(i).firstElementChild.style.display = "unset";
      recordAll.item(i).lastElementChild.style.display = "none";
    }
  } else {
    selectAllBtn.firstElementChild.style.display = "none";
    selectAllBtn.lastElementChild.style.display = "unset";
    recordAll = document.querySelectorAll(".record .select");
    for (let i = 0; i < recordAll.length; i++) {
      recordAll.item(i).firstElementChild.style.display = "none";
      recordAll.item(i).lastElementChild.style.display = "unset";
    }
  }
});
*/
