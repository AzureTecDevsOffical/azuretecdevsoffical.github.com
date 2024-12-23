/* 
Copyright 2024 AzureTecDevs
Use of this code comes with the Blue Oak Model license; if not included contact azuretecdevs@gmail.com.
*/
class WebPage {
    getURLParameter(name) {
        const urlParams = new URLSearchParams(window.location.search);
        return urlParams.get(name);
    }
    getTitle() {
        return document.title;
    }
    getHtml() {
        return document.documentElement.outerHTML;
    }
}