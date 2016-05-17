
function upload(blobOrFile) {
 var xhr = new XMLHttpRequest();
 xhr.open('POST', 'http://10.245.251.161:2033/upload', false);
 fd=new FormData();
 fd.append('mof',blobOrFile);
 xhr.send(fd);
}

function process() {
  var blob = file;
  const BYTES_PER_CHUNK = 1024 * 1024;
  // 1MB chunk sizes.
  const SIZE = blob.size;

  var start = 0;
  var end = BYTES_PER_CHUNK;
  while (start < SIZE) {
   if ('mozSlice' in blob) {
    var chunk = blob.mozSlice(start, end);
   } else {
    var chunk = blob.slice(start, end);
   }
   upload(chunk);
   start = end;
   end = start + BYTES_PER_CHUNK;
  }
  self.postMessage(blob.name + " Uploaded Succesfully");
}

self.onmessage = function(e) {
  file = e.data;
  process();
}
