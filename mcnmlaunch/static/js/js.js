(function($, app, window) {

	$('section').removeClass('active');

	setTimeout(function(){
	  	var next = $('.section_0 .nextScroll');
	  	TweenLite.to(next, 0.3, {css:{'opacity':'1'}, onComplete:function(){
	  		setTimeout(function(){
	  			var hint = $('.section_0 .scroll-hint');
				TweenLite.to(hint, 1, {css:{'bottom':'20px'}, ease:Bounce.easeOut });
				$('.section_0 .scroll-hint').addClass('active');
	  		}, 0);
			TweenLite.to(next, 1, {css:{'bottom':'20px'}, ease:Bounce.easeOut });
		}});
	}, 1000);

	app.globalEvents = function (app, selector) {
		var $wrapper = $(selector || window.document);
		$wrapper
				.on('click', '#path a, .section_5 .nav .list a, .gotoThrd, .gotoFour, .gotoFive, .gotoSix', function (e){
					e.preventDefault();
					app.gotoSection($(this), $('section'));
				})
				.on('click', 'a.btn-big', function (e){
					e.preventDefault();
					app.gotoSection($(this), $('section'));

						$('.btn-big_2').addClass('hidden');
						$('section.section_5 .nav').addClass('hidden');
						$('.form').removeClass('hidden');
						$('.btn-big').removeClass('hidden');


				})
				.on('mouseenter mouseleave', '.section_1 .part', function (e){
					app.section_1Hover($(this));
				})
				.on('mouseenter', '.section_2 .img', function (e){
					app.section_2HoverOn($(this));
				})
				.on('mouseleave', '.section_2 .img', function (e){
					app.section_2HoverOut($(this));
				})
				.on('click', '.section_3 .eye', function (e){
					e.preventDefault();
					app.section_2Click($(this), $(this).closest('section'));
				})
				.on('click', '.section_5 .btn-big_2', function (e){
					e.preventDefault();
					app.yesOfCourse($(this), $(this).closest('section'));
				})
				.on('click', '.checkbox', function (e){
					app.toggleCheckbox($(this));
				})
				.on('click', '.section_0 .nextScroll', function (e){
					e.preventDefault();
					TweenLite.to($(window), 0.6, {scrollTo:{y:$('.section_1').offset().top}, ease:Power2.easeOut});
				});

	};

	app.globalLogic = function(spec) {

		this.gotoSection = function($this, $sections){
			var rel = $this.data('rel');
			var currSection;
			$sections.each(function(){
				if($(this).data('rel')===rel){
					$('section').removeClass('active');
					currSection = $(this);
					currSection.addClass('active');
				}
			});
            TweenLite.to($(window), 0, {scrollTo:{y:currSection.data('skrollr')}, ease:Power2.easeOut, onComplete:function(){
                if (rel == '2') {
                    setTimeout(function(){ $('.phone.pic1').removeClass('down'); }, 200);
                    setTimeout(function(){ $('.phone.pic2').removeClass('down'); }, 300);
                    setTimeout(function(){ $('.phone.pic3').removeClass('down'); }, 350);
                }
            }});
		};

		this.section_1Hover = function($this){

			$this.find('.q_link').toggleClass('active');
		};

		this.section_2HoverOn = function($this){
			$this.addClass('active');
			$this.find('.phone').addClass('down');
		};

		this.section_2HoverOut = function($this){
			$this.removeClass('active');
			$this.find('.phone').removeClass('down');
		};

		this.section_2Click = function($this, $parent){
			var cLeft = $parent.find('.circle.left');
			var cRight = $parent.find('.circle.right');
			TweenLite.to($this.find('.tip'), 0.1, {css:{'opacity':'0', 'cursor':'default'}, onComplete:function(){
				TweenLite.to($this, 0.3, {css:{'opacity':'0', 'cursor':'default'}, onComplete:function(){
					TweenLite.to(cLeft, 1, {css:{'margin-left':'-20px'}, ease:Power2.easeInOut});
					cLeft.animate({'margin-left':'-20px'});
					cRight.animate({'margin-right':'-20px'});
					TweenLite.to(cRight, 1, {css:{'margin-right':'-20px'}, ease:Power2.easeInOut});
				}});
			}});
		};

		this.yesOfCourse = function($this, $parent){
			$this.addClass('hidden');
			$parent.find('.nav').addClass('hidden');
			$parent.find('.form').removeClass('hidden');
			$parent.find('.btn-big').removeClass('hidden');
		};

		this.toggleCheckbox = function($this){

			$this.find('i').toggleClass('active');
		};

		this.focusField = function($this){
			if(!$this.data('default')){
				$this.data('default', $this.val());
				$this.val('');
			} else if($this.val()===$this.data('default')) {
				$this.val('');
			}
		};

		this.blurField = function($this){
			if($this.val()===''||$this.val()===$this.data('default')){
				$this.val($this.data('default'));
				$this.removeClass('filled');
			} else {
				$this.addClass('filled');
			}
		}

		this.fieldFill = function($this){

			$this.addClass('filled');
		}



		return this;
	};

})(jQuery, window.fbrApp || (window.fbrApp = {}), window);

$(function(){

	fbrApp.globalEvents(new fbrApp.globalLogic(), window.document);

	//

	function preloadImages(img){
		var	$imga = img;
		$imga.each(function(i) {
			var $img = $(this);
			$('<img/>').load(function() {
				imgOperations($imga);
				imgResize();
			}).attr('src',$img.attr('src'));
		});
	}

	function setSize(img){

		var w = img.width(),
			h = img.height();

			img.data('size', 'set');

			if(w>h){
				img.css({'width':'100%'});
				img.css({'height':'auto'});
				img.data('ratio', (parseInt((w/h)*100)).toString());
			} else {
				img.css({'height':'100%'});
				img.css({'width':'auto'});
				img.data('ratio', (parseInt((h/w)*100)).toString());
			}

		return img;
	}

	function imgOperations(img){
		var _img = setSize(img);
		_img.removeClass('vhidden');
	}

	function imgResize(){

		$('.preloaded').each(function(){

			var thisImg;

			if($(this).data('size')!='set'){
				thisImg = setSize($(this));
			} else {
				thisImg = $(this);
			}

			if(thisImg.width()<thisImg.parent().width()){
				thisImg.css({'width':'100%','height':'auto'});
			}

			if(thisImg.height()<thisImg.parent().height()){
				thisImg.css({'height':'100%','width':'auto'});
			} else {
				if($('html').hasClass('touch')){
					thisImg.css({'width':'100%','height':'auto'}); // TODO
				}
			}

		});

	}

	// SCROLL HANDLER

	preloadImages($('.preloaded'));

	var centerH = function(target){
		target.each(function(){
			var $this = $(this);
			var halfWidth = $this.outerWidth(true)/2;
			var winHalfWidth;

			var origin;

			if($this.hasClass('by_parent')){
				origin = $this.parent();
			} else {
				origin = $(window);
			}

			winHalfWidth = origin.width()/2;

			var leftPos = winHalfWidth-halfWidth;

			if($this.hasClass('center_h_1-3')) {
				winHalfWidth = (origin.width()-150)/4;
				leftPos = winHalfWidth-halfWidth;
				$this.css({'left':leftPos});
			} else if($this.hasClass('center_h_2-3')) {
				winHalfWidth = ((origin.width()/4)*3)+75;
				leftPos = winHalfWidth-halfWidth;
				$this.css({'left':leftPos});
			} else {
				$this.css({'left':leftPos});
			}

		});
	};

	var centerV = function(target){
		target.each(function(){
			var $this = $(this);
			var halfHeight = $this.outerHeight(true)/2;
			var winHalfHeight;

			if($this.hasClass('by_parent')){
				winHalfHeight = $this.parent().height()/2;
			} else {
				winHalfHeight = $(window).height()/2;
			}

			var topPos = winHalfHeight-halfHeight;
			$this.css({'top':topPos});
		});
	};

	var wSome = function($this){
		$this.each(function(){
			var $this = $(this);
			var pW = $this.parent().width()/3;
			$this.css({'width':pW});
		});
	}

	var wSomeTwo = function($this){
		$this.each(function(){
			var $this = $(this);
			var pW = $this.parent().width()/2 - 100;
			$this.css({'width':pW});
		});
	}

	window.globalReflow = function(){
		centerV($('.center_v, #owl-demo'));
		centerH($('.center_h, #owl-demo'));
		wSome($('.w1_3'));
		wSomeTwo($('.w1_thr'));
	};

	window.globalReflow();

	//

	$(window).resize(function(){
		imgResize();
		window.globalReflow();
	});








});



$(document).ready(function(){
	$( ".s3" ).click(function() {
		setTimeout(function() {
			var detailHand = $('section.section_3 .eye .tip.icon, section.section_3 .eye .tip.txt');
			detailHand.fadeIn(500);
		}, 1500);
	});
});
































/***************************/
//@Author: Adrian "yEnS" Mato Gondelle & Ivan Guardado Castro
//@website: www.yensdesign.com
//@email: yensamg@gmail.com
//@license: Feel free to use it, but keep this credits please!
/***************************/

$(document).ready(function(){
	//global vars
	var form = $("#customForm");
	var name = $("#name");
	var nameInfo = $("#nameInfo");
	var companyname = $("#companyname");
	var companynameInfo = $("#companynameInfo");
	var email = $("#email");
	var emailInfo = $("#emailInfo");
	var phone = $("#phone");
	var phoneInfo = $("#phoneInfo");

	//On blur
	name.blur(validateName);
	companyname.blur(validateCompanyName);
	email.blur(validateEmail);
	phone.blur(validatePhone);
	//On key press
	name.keyup(validateName);
	companyname.keyup(validateCompanyName);
	phone.keyup(validatePhone);
	//On Submitting
	form.submit(function(){
		if(validateName() & validateCompanyName() & validatePhone() & validateEmail()) {
			// Prepare query string and send AJAX request
			$.ajax({
	            type: "POST",
	            url: "/save",
				data: {
					'name': name.val(),
					'company': companyname.val(),
					'email': email.val(),
					'phone': phone.val()
				},
				success: function(data) {
					if (data.success) {
                        $('.response').removeClass('hidden');						

						name.val('')
                        companyname.val('')
                        email.val('')
                        phone.val('')

                        $("input[type=submit]").addClass('inactive').prop("disabled", true);
	                    _gaq.push(["_trackPageview", "/#my-ajax-page-store"]);
					}
				},
		        error: function (xhr, str) {
		            alert("Возникла ошибка!");
		        }			
			});
			return false;
		}
		else
			return false;
	});


	$(document).ready(function (){
		validate();
		$('#name, #companyname, #phone, #email').change(validate);

		// footer menu hover
		$( "footer .inner li" ).hover(
			function() {
			$( this ).addClass( "hover" );
		}, function() {
			$( this ).removeClass( "hover" );
		}
		);

	});

	function validate(){
		if ($('#name').val().length   >   0   &&
			$('#companyname').val().length  >   0   &&
			$('#phone').val().length  >   0   &&
			$('#email').val().length    >   0 && validateEmail() && validateName() && validatePhone() && validateCompanyName()) {
			$("input[type=submit]").removeClass('inactive').prop("disabled", false);
		}
		else {
			$("input[type=submit]").addClass('inactive').prop("disabled", true);
		}
	}

	$('input[name=name]').keyup(function() { validate() });
	$('input[name=companyname]').keyup(function() { validate() });
	$('input[name=phone]').keyup(function() { validate() });
	$('input[name=email]').keyup(function() { validate() });


	//validation functions
	function validateEmail(){
		//testing regular expression
		var a = $("#email").val();
		var filter = /^[a-zA-Z0-9]+[a-zA-Z0-9_.-]+[a-zA-Z0-9_-]+@[a-zA-Z0-9]+[a-zA-Z0-9.-]+[a-zA-Z0-9]+.[a-z]{2,4}$/;
		//if it's valid email
		if(filter.test(a)){
			email.removeClass("error");
			emailInfo.text("");
			emailInfo.removeClass("error");
			return true;
		}
		//if it's NOT valid
		else{
			email.addClass("error");
			emailInfo.text("");
			emailInfo.addClass("error");
			return false;
		}
	}

	function validatePhone(){
		//testing regular expression
		var a = $("#phone").val();
		var filter = /^\s*[0-9-+,\s]+\s*$/;
		//if it's valid phone
		if(phone.val().length < 16){
			phone.addClass("error");
			phoneInfo.text("");
			phoneInfo.addClass("error");
			return false;
		}
		//if it's valid
		else{
			phone.removeClass("error");
			phoneInfo.text("");
			phoneInfo.removeClass("error");
			return true;
		}
	}


	function validateName(){
		//if it's NOT valid
		if(name.val().length < 4){
			name.addClass("error");
			nameInfo.text("");
			nameInfo.addClass("error");
			return false;
		}
		//if it's valid
		else{
			name.removeClass("error");
			nameInfo.text("");
			nameInfo.removeClass("error");
			return true;
		}
	}

	function validateCompanyName(){
		//if it's NOT valid
		if(companyname.val().length < 4){
			companyname.addClass("error");
			companynameInfo.text("");
			companynameInfo.addClass("error");
			return false;
		}
		//if it's valid
		else{
			companyname.removeClass("error");
			companynameInfo.text("");
			companynameInfo.removeClass("error");
			return true;
		}
	}

	
	
});


// jQuery Mask Plugin v1.3.2
// github.com/igorescobar/jQuery-Mask-Plugin
(function(c){var w=function(a,d,e){var f=this;a=c(a);var l;d="function"==typeof d?d(a.val(),void 0,a,e):d;f.init=function(){e=e||{};f.byPassKeys=[8,9,16,36,37,38,39,40,46,91];f.translation={0:{pattern:/\d/},9:{pattern:/\d/,optional:!0},"#":{pattern:/\d/,recursive:!0},A:{pattern:/[a-zA-Z0-9]/},S:{pattern:/[a-zA-Z]/}};f.translation=c.extend({},f.translation,e.translation);f=c.extend(!0,{},f,e);a.each(function(){!1!==e.maxlength&&a.attr("maxlength",d.length);a.attr("autocomplete","off");g.destroyEvents();
g.events();g.val(g.getMasked())})};var g={events:function(){a.on("keydown.mask",function(){l=g.val()});a.on("keyup.mask",g.behaviour);a.on("paste.mask",function(){setTimeout(function(){a.keydown().keyup()},100)})},destroyEvents:function(){a.off("keydown.mask").off("keyup.mask").off("paste.mask")},val:function(v){var d="input"===a.get(0).tagName.toLowerCase();return 0<arguments.length?d?a.val(v):a.text(v):d?a.val():a.text()},behaviour:function(a){a=a||window.event;if(-1===c.inArray(a.keyCode||a.which,
f.byPassKeys))return g.val(g.getMasked()),g.callbacks(a)},getMasked:function(){var a=[],c=g.val(),b=0,q=d.length,h=0,l=c.length,k=1,r="push",m=-1,n,s;e.reverse?(r="unshift",k=-1,n=0,b=q-1,h=l-1,s=function(){return-1<b&&-1<h}):(n=q-1,s=function(){return b<q&&h<l});for(;s();){var t=d.charAt(b),u=c.charAt(h),p=f.translation[t];p?(u.match(p.pattern)?(a[r](u),p.recursive&&(-1==m?m=b:b==n&&(b=m-k),n==m&&(b-=k)),b+=k):p.optional&&(b+=k,h-=k),h+=k):(a[r](t),u==t&&(h+=k),b+=k)}return a.join("")},callbacks:function(f){var c=
g.val(),b=g.val()!==l;if(!0===b&&"function"==typeof e.onChange)e.onChange(c,f,a,e);if(!0===b&&"function"==typeof e.onKeyPress)e.onKeyPress(c,f,a,e);if("function"===typeof e.onComplete&&c.length===d.length)e.onComplete(c,f,a,e)}};f.remove=function(){g.destroyEvents();g.val(f.getCleanVal()).removeAttr("maxlength")};f.getCleanVal=function(){for(var a=[],c=g.val(),b=0,e=d.length;b<e;b++)f.translation[d.charAt(b)]&&a.push(c.charAt(b));return a.join("")};f.init()};c.fn.mask=function(a,d){return this.each(function(){c(this).data("mask",
new w(this,a,d))})};c.fn.unmask=function(){return this.each(function(){try{c(this).data("mask").remove()}catch(a){}})};c("input[data-mask]").each(function(){var a=c(this),d={};"true"===a.attr("data-mask-reverse")&&(d.reverse=!0);"false"===a.attr("data-mask-maxlength")&&(d.maxlength=!1);a.mask(a.attr("data-mask"),d)})})(window.jQuery||window.Zepto);

$(function() {
	$('.phone').mask('+0 000 00 000 00');
});