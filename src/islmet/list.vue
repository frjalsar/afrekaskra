<template>
<div class="h_iframe">
    <iframe src="https://fri.is/afrekaskra/MetOfl/islandsmet.htm" id="contentFrame" frameborder="0" scrolling="no" onload="resizeIframe(this)" style="height:62750px;"></iframe>
</div>
</template>

<script>
export default {
    name: "IslmetList",
    data() {
        return {
            isReady: false
        }
    },
      mounted() {
    //let extScript = document.createElement('script')
    //extScript.setAttribute('src', 'static/extScript.js')
    //document.head.appendChild(extScript)

    var scriptTag = document.createElement("script");
    scriptTag.type = "text/javascript";
    scriptTag.text = `function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.documentElement.scrollHeight + 'px';
  }`;
    document.body.appendChild(scriptTag);
  }
}
</script>

<style scoped>
.html, body {
    height:100%;
    width:100%;
    margin:0;
}
.h_iframe iframe {
    width:100%;
    height:100%;
}
.h_iframe {
    height: auto;
    width:100%;
}

.contentFrame {        
    border: none;
    padding: 0;
    margin: 0;
    background-color: pink;
    height: 100%;
    vertical-align:bottom;
}
</style>