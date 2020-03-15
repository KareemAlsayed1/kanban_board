
var boards = dragula([ document.getElementById("todo_body"), 
document.getElementById("doing_body"),document.getElementById("done_body"),document.getElementById("accordionDoing"),
document.getElementById("accordionTodo"),document.getElementById("accordionDone"),
document.getElementById("accordionDoing")],{
        isContainer: function (el) {
          return false; 
        },
        moves: function (el, source, handle, sibling) {
          if (el.id == 'task' || el.id == 'accordionDoing' ||el.id == 'accordionDone' ||el.id == 'accordionTodo'){
                return true; 
          }else{
                return true;
          }
        },
        accepts: function (el, target, source, sibling) {
                if (target.id == "accordionTodo" || target.id == "todo" || 
                target.id == "accordionDoing" || target.id == "doing" || 
                target.id == "accordionDone" || target.id == "done" ){
                        return false; 
                }
          return true;
        },
        invalid: function (el, handle) {
          return false; 
        },
        direction: 'vertical',             
        copy: false,                      
        copySortSource: false,             
        revertOnSpill: false,              
        removeOnSpill: false,             
        mirrorContainer: document.body,    
        ignoreInputTextSelection: true     
      })
.on('drop', function (el, target) {
swtich_request (target.title, el.title)
})

function swtich_request (status, id){
let xhr = new XMLHttpRequest();
xhr.open("POST", "/switch/"+status+'/'+id.toString());
xhr.send ();
location.reload();
}

