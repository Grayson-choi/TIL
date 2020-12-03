// 주소 요청
function request(url) {
  
  option = {
    method: 'GET'
  }
  
  return fetch(url, option)
    .then(function (res) {
      return res.json()
    })
    .then(result => result['data'])
    .catch(err => console.error(err))
}


const btn = document.querySelector('.click')
btn.addEventListener('click', event => {
  const rank_url = 'https://www.naver.com/srchrank?frm=main'
  
  request(rank_url).then(res => {
    let table = document.querySelector('table');
    let elem_length = document.querySelectorAll('td');
    
    let items = document.querySelectorAll('.item');
 

    document.querySelector('tbody').remove()
    const elem = document.createElement('tbody')
    table.appendChild(elem);
    for (data of res){
      // elem.parentNode.removeChild(elem);
      
      makingTable(elem, data.rank, data.keyword);

    }
    
    // 이미 요소들이 생성되어 있으면 요소 삭제
    if (elem_length.length > 20){
      for(i = 0; i < 20; i++){    
          // console.log(items[i]);
          table.removeChild(items[i]);
        }
      }   
  })
})

function makingNews(num, rank, keyword){
  let td_news_num = document.createElement('td');
  td_news_num.innerText = num;

  let news_link = document.createElement('a');
  news_link.innerText = `${rank}등 검색어 관련기사 ${keyword}`;

  let newsTr = document.createElement('tr');
  // newsTr.innerText = `${rank}등 검색어 관련기사`;
  newsTr.align = 'center';
  newsTr.setAttribute("class", `news${rank}`);
  newsTr.style.display = "none";
  newsTr.append(td_news_num);
  newsTr.append(news_link);
  return newsTr
}


function makingTable(elem, rank, keyword) {

  const search_url = 'https://search.naver.com/search.naver?query='
  let key_search = document.createElement('button');
  
  key_search.innerText = keyword;

  let td_rank = document.createElement('td');
  td_rank.innerText = rank;
  
  let tr = document.createElement('tr');
  tr.align = 'center';
  tr.append(td_rank);
  tr.append(key_search);
  tr.setAttribute("class", `item${rank}`);
  
  let newsTr1 = makingNews(1, rank, keyword);
  let newsTr2 = makingNews(2, rank, keyword);
  let newsTr3 = makingNews(3, rank, keyword);


  elem.append(tr);
  elem.append(newsTr1);
  elem.append(newsTr2);
  elem.append(newsTr3);


  const itemBtn = document.querySelector(`.item${rank}`);
  itemBtn.addEventListener('click', event => {
    let newsBtn = document.querySelectorAll(`.news${rank}`);
    newsBtn.forEach(function(x){
      if (x.style.display === "none") {
        x.style.display = "table-row";
      } else {
        x.style.display = "none";
      }
    });
   
  });

};
