function PumukitEdit(runtime, element) {
    $(element).find('.pumukit-save-button').bind('click', function() {
	var data = {
	    'video_id': $('#video_id').val(),
	};
	var handlerUrl = runtime.handlerUrl(element, 'pumukit_submit');
	$('.xblock-editor-error-message', element).html();
	$('.xblock-editor-error-message', element).css('display', 'none');
	$.post(handlerUrl, JSON.stringify(data)).done(function(response) {
	    if (response.result === 'success') {
		window.location.reload(false);
	    } else {
		$('.xblock-editor-error-message', element).html('Error: '+response.message);
		$('.xblock-editor-error-message', element).css('display', 'block');
	    }
	});
    });

    $(element).find('.pumukit-cancel-button').bind('click', function() {
	runtime.notify('cancel', {});
    });

    $(element).find('.tab-url').bind('click', function(event) {
	$('.component-tab-url').show();
	$('.component-tab-url').removeClass('is-inactive');
	$('.tab-url').addClass('current');

	$('.component-tab-manager').hide();
	$('.component-tab-manager').addClass('is-inactive');
	$('.tab-manager').removeClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').hide();
	$('.component-tab-upload').addClass('is-inactive');
	$('.tab-upload').removeClass('current');

	$('.component-tab-recorder').hide();
	$('.component-tab-recorder').addClass('is-inactive');
	$('.tab-recorder').removeClass('current');

	$('.modal-lg').removeClass('modal-lg-Pumukit');
	$('.modal-content').removeClass('modal-content-Pumukit');
	$('.edit-xblock-modal').removeClass('edit-xblock-modal-Pumukit');
	$('.settings-list').removeClass('settings-list-Pumukit');
	$('.tabs-wrapper').removeClass('tabs-wrapper-Pumukit');
	$('.wrapper-comp-settings').removeClass('wrapper-comp-settings-Pumukit');
    });

    $(element).find('.tab-manager').bind('click', function(event) {
	$('.component-tab-url').hide();
	$('.component-tab-url').addClass('is-inactive');
	$('.tab-url').removeClass('current');

	$('.component-tab-manager').show();
	$('.component-tab-manager').removeClass('is-inactive');
	$('.tab-manager').addClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').hide();
	$('.component-tab-upload').addClass('is-inactive');
	$('.tab-upload').removeClass('current');

	$('.component-tab-recorder').hide();
	$('.component-tab-recorder').addClass('is-inactive');
	$('.tab-recorder').removeClass('current');

	$('.modal-lg').addClass('modal-lg-Pumukit');
	$('.modal-content').addClass('modal-content-Pumukit');
	$('.edit-xblock-modal').addClass('edit-xblock-modal-Pumukit');
	$('.settings-list').addClass('settings-list-Pumukit');
	$('.tabs-wrapper').addClass('tabs-wrapper-Pumukit');
	$('.wrapper-comp-settings').addClass('wrapper-comp-settings-Pumukit');
    });

    $(element).find('.tab-upload').bind('click', function(event) {
	$('.component-tab-url').hide();
	$('.component-tab-url').addClass('is-inactive');
	$('.tab-url').removeClass('current');

	$('.component-tab-manager').hide();
	$('.component-tab-manager').addClass('is-inactive');
	$('.tab-manager').removeClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').show();
	$('.component-tab-upload').removeClass('is-inactive');
	$('.tab-upload').addClass('current');

	$('.component-tab-recorder').hide();
	$('.component-tab-recorder').addClass('is-inactive');
	$('.tab-recorder').removeClass('current');

	$('.modal-lg').addClass('modal-lg-Pumukit');
	$('.modal-content').addClass('modal-content-Pumukit');
	$('.edit-xblock-modal').addClass('edit-xblock-modal-Pumukit');
	$('.settings-list').addClass('settings-list-Pumukit');
	$('.tabs-wrapper').addClass('tabs-wrapper-Pumukit');
	$('.wrapper-comp-settings').addClass('wrapper-comp-settings-Pumukit');
    });

    $(element).find('.tab-recorder').bind('click', function(event) {
	$('.component-tab-url').hide();
	$('.component-tab-url').addClass('is-inactive');
	$('.tab-url').removeClass('current');

	$('.component-tab-manager').hide();
	$('.component-tab-manager').addClass('is-inactive');
	$('.tab-manager').removeClass('current');

	$('.component-tab-select').hide();
	$('.component-tab-select').addClass('is-inactive');
	$('.tab-select').removeClass('current');

	$('.component-tab-upload').hide();
	$('.component-tab-upload').addClass('is-inactive');
	$('.tab-upload').removeClass('current');

	$('.component-tab-recorder').show();
	$('.component-tab-recorder').removeClass('is-inactive');
	$('.tab-recorder').addClass('current');

	$('.modal-lg').addClass('modal-lg-Pumukit');
	$('.modal-content').addClass('modal-content-Pumukit');
	$('.edit-xblock-modal').addClass('edit-xblock-modal-Pumukit');
	$('.settings-list').addClass('settings-list-Pumukit');
	$('.tabs-wrapper').addClass('tabs-wrapper-Pumukit');
	$('.wrapper-comp-settings').addClass('wrapper-comp-settings-Pumukit');
    });

    window.addEventListener('message', function (event) {
        if(event.data === 'enableMoodlePRAdd?'){
            event.source.postMessage({'moodlepradd':'OK'}, '*');
        }

        if (!event.data.mmId) {
            return;
        }

	    $('#video_id').val(event.data.mmId);

    }, false);

}

function show_hide_collection(id) {
    id = '#' + id;
    if ($(id).hasClass('Pumukit-list-collection-hide')) {
	$(id).hide();
	$(id).addClass('Pumukit-list-collection-show');
	$(id).removeClass('Pumukit-list-collection-hide');
    } else {
	$(id).show();
	$(id).removeClass('Pumukit-list-collection-show');
	$(id).addClass('Pumukit-list-collection-hide');
    }
    return false;
}

function show_hide_child(id) {
    id = '#' + id;
    if ($(id).hasClass('Pumukit-list-child-hide')) {
	$(id).hide();
	$(id).addClass('Pumukit-list-child-show');
	$(id).removeClass('Pumukit-list-child-hide');
    } else {
	$(id).show();
	$(id).removeClass('Pumukit-list-child-show');
	$(id).addClass('Pumukit-list-child-hide');
    }
    return false;
}

function show_hide_grandchild(id) {
    id = '#' + id;
    if ($(id).hasClass('Pumukit-list-grandchild-hide')) {
	$(id).hide();
	$(id).addClass('Pumukit-list-grandchild-show');
	$(id).removeClass('Pumukit-list-grandchild-hide');
    } else {
	$(id).show();
	$(id).removeClass('Pumukit-list-grandchild-show');
	$(id).addClass('Pumukit-list-grandchild-hide');
    }
    return false;
}
