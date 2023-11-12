let showImg = document.querySelector('.show-img');
let upload = document.querySelector('#file-input');
let btn = document.querySelector('.box > button');
let form = document.querySelector('form');
let result = document.querySelector('.result');
let blobImage;

upload.addEventListener('change', e => {
	if (!e.target.files.length) return;

	const reader = new FileReader();

	reader.onload = e => {
		if (!e.target.result) return;

		let img = document.createElement('img');
		img.id = 'image';
		img.src = e.target.result;

		showImg.innerHTML = '';
		showImg.appendChild(img);

		btn.classList.remove('hide');
	};

	blobImage = e.target.files[0];
	reader.readAsDataURL(blobImage);
});

form.addEventListener('submit', e => {
	e.preventDefault();

	if (!blobImage) return;

	const request = new FormData();
	request.append('image', blobImage);

	fetch('/predict', { method: 'POST', body: request })
		.then(res => res.json())
		.then(({ prediccion }) => {
			result.innerHTML = `El dígito detectado es: ${prediccion}`;
		});
});
