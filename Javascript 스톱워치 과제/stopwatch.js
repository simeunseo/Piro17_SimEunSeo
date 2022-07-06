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
const selectAllBtn = document.querySelector(".check-all"); //전체 선택 버튼
let btnList = document.querySelectorAll(".check"); //모든 기록들의 체크 버튼 리스트
const trashBtn = document.querySelector(".trash");
let allCheckedFlag = 0;

//타이머 start버튼 기능
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

//타이머 stop버튼 기능
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
  //현재 기록 가져와서 기록하기
  record.appendChild(newRecord);
  newRecord.lastElementChild.lastElementChild.innerText =
    lapseMillisecond.innerText;
  newRecord.lastElementChild.firstElementChild.innerText =
    lapseSecond.innerText;
  btnList = document.querySelectorAll(".check");
});

//타이머 reset버튼 기능
resetBtn.addEventListener("click", function () {
  millisecond = 0;
  second = 0;
  lapseMillisecond.innerText = "00";
  lapseSecond.innerText = "00";
  clearInterval(intervalID);
});

//기록 전체 선택 기능
selectAllBtn.addEventListener("click", function () {
  if (selectAllBtn.checked == true) {
    //체크가 안되어있다면 체크한다
    selectAllBtn.checked = true;
    for (let j = 0; j < btnList.length; j++) {
      btnList[j].checked = true;
    }
    allCheckedFlag = 1;
  } else {
    //이미 체크되어있다면 모두 해제한다
    selectAllBtn.checked = false;
    for (let j = 0; j < btnList.length; j++) {
      btnList[j].checked = false;
    }
    allCheckedFlag = 0;
  }
});

for (let i = 0; i < btnList.length; i++) {
  if (btnList[i].checked == false) {
    allCheckedFlag = 0;
    selectAllBtn.checked = false;
  }
}

trashBtn.addEventListener("click", function () {
  for (let k = 0; k < btnList.length; k++) {
    //체크된 기록이라면
    if (btnList[k].checked == true) {
      btnList[k].parentElement.parentElement.remove();
    }
  }
});
