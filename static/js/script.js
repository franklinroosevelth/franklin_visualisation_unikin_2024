function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function(e) {
            $('.image-upload-wrap').hide();
            $('.file-upload-image').attr('src', e.target.result);
            $('.file-upload-content').show();
            $('.image-title').html(input.files[0].name);
        };

        reader.readAsDataURL(input.files[0]);
    } else {
        removeUpload();
    }
}

function removeUpload() {
    $('.file-upload-input').replaceWith($('.file-upload-input').clone());
    $('.file-upload-content').hide();
    $('.image-upload-wrap').show();
    $('.img-detect').attr("src", "");
}

$('.image-upload-wrap').on('dragover', function () {
    $('.image-upload-wrap').addClass('image-dropping');
});

$('.image-upload-wrap').on('dragleave', function () {
    $('.image-upload-wrap').removeClass('image-dropping');
});

function detect_objects() {
    var formData = new FormData();
    var fileInput = document.querySelector('.file-upload-input');
    var file = fileInput.files[0];
    formData.append('file', file);

    $.ajax({
        type: "POST",
        url: "/img_b64",
        data: formData,
        processData: false,
        contentType: false,
        dataType: "json",
        success: function(response) {
            console.log(response.img_b64);
            $('.img-detect').attr("src", "data:image/png;base64," + response.img_b64);
        },
        error: function(xhr, status, error) {
            console.error("Error:", status, error);
        }
    });
}
