
$('.catalog__price').text((i, text) => {
    const [ price, currency ] = text.split(' ');
    return `${(+price).toLocaleString()} ${currency}`;
  });
