function ajaxSend(url, params) {
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
        .then(response => response.json())
        .then(json => render(json))
        .catch(error => console.error(error))
}

const forms = document.querySelector('form[name=filter]');

forms.addEventListener('submit', function (e) {
    e.preventDefault();
    let url = this.action;
    let params = new URLSearchParams(new FormData(this)).toString();
    ajaxSend(url, params);
});

function render(data) {
    let template = Hogan.compile(html);
    let output = template.render(data);

    const div = document.querySelector('.catalog__product>.row');
    div.innerHTML = output;
}

let html = '\
{{#movies}}\
<div class="col-xl-3 col-lg-4 col-md-4 col-sm-6 col-6">\
<div class="catalog__col d-flex  flex-column position-relative">\
    <img src="/{{img__img}}" alt="catalog__photo" class="catalog__img" draggable="false">\
    <a href="/catalog/about/{{id}}" class="catalog__name">{{ title }}</a>\
    <div class="d-flex catalog__buy justify-content-end align-items-center">\
        <span class="catalog__price">{{ price }} ₴</span>\
        <button class="border-0 button__catalog">\
        </button>\
        <button class="border-0 button__catalog">\
        </button>\
    </div>\
    <button class="position-absolute top-0 end-0 border-0 catalog__button__like">\
    </button>\
</div>\
</div>\
{{/movies}}'


