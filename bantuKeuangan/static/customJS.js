//menggunakan csrf token dengan ajax, tidak melalui form
// ex
/*
var csr=getCookie('csrftoken'); -> di diklarasikan dulu
onSubmit: function (param) {
        param.csrfmiddlewaretoken=csr;
        return $(this).form('validate');
    }, -> di jadikan parameter value untuk form
*/
function getCookie(name){
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// untuk auto save create dan update
// fm => selectoor untuk form yang akan di submit ex 'fModulBla'->string
// url => url untuk prosessing data form ex 'simrs/modulsave'
// model => model yang akan digunakan untuk menyimpan ke database ex 'klinik'->string
// datagrid => Optional (digunakan untuk merefresh datagrid yang ditentukan ketika form berhasi disimpan)->string
// dialog => Optional (digunakan untuk menutup dialog datagrid yang ditentukan ketika form berhasi disimpan)->string
function saveData(fm,url,dbmodel,datagrid,dialog,paket){
    var kon;
    var csr=getCookie('csrftoken');
    var yy=$('#'+fm).form('submit', {
    url: url,
    onSubmit: function (param) {
        param.csrfmiddlewaretoken=csr;
        param.dbmodel = dbmodel;
        param.paket = paket;
        return $(this).form('validate');
    },
    success: function (result) {
        var result = eval('(' + result + ')');
        if (result.errorMsg) {
            $.messager.show({
                title: 'Error',
                msg: result.errorMsg
            });
        } else {
            //console.log(result);
            if(dialog!="undefined" || dialog!=""){
               $('#'+dialog).dialog('close');
            }
            if(datagrid!="undefined" || dialog!=""){
               $('#'+datagrid).datagrid('reload');
            }
            $.messager.show({
                title: 'Sukses',
                msg: result.success
            });
            
        }
    }
    });
    //console.log(yy)
    
}
//Date formatter untuk jeasyui
// Format menggunakan standar dd/mm/yy
// karena di define di global, seluruh easyui-datebox akan terpengaruh

$.extend($.fn.datebox.defaults, {
    formatter: function (date) {
        var y = date.getFullYear();
        var m = date.getMonth() + 1;
        var d = date.getDate();
        return (d < 10 ? ('0' + d) : d) + '/' + (m < 10 ? ('0' + m) : m) + '/' + y;
    },
    parser: function (s) {
        if (!s)
            return new Date();
        var ss = s.split('/');
        var d = parseInt(ss[0], 10);
        var m = parseInt(ss[1], 10);
        var y = parseInt(ss[2], 10);
        if (!isNaN(y) && !isNaN(m) && !isNaN(d)) {
            return new Date(y, m - 1, d);
        } else {
            return new Date();
        }
    }
});
//Tanggal Hari ini
// format dd/mm/yy
function tanggalHariIni(format=""){
    if(format==""){
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();

        today = dd + '/' + mm + '/' + yyyy;
        return today;
    }else if(format=="fullwaktu"){
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        var h=("0" + today.getHours()).slice(-2);
        var m=("0" + today.getMinutes()).slice(-2);
        var s=("0" + today.getSeconds()).slice(-2);
        today = dd + '/' + mm + '/' + yyyy +" "+h + ":"+m+":"+s;
        return today;
    }
}
function debug(){

}

$.extend($.fn.textbox.methods, {
	show: function(jq){
		return jq.each(function(){
			$(this).next().show();
		})
	},
	hide: function(jq){
		return jq.each(function(){
			$(this).next().hide();
		})
	}
});
$.extend($.fn.panel.methods, {
	showMask: function(jq, msg){
		return jq.each(function(){
			var pal = $(this).panel('panel');
			if (pal.css('position').toLowerCase() != 'absolute'){
				pal.css('position','relative');
			}
			var borderSize = parseInt(pal.css('padding'))+1;
			var m = pal.children('div.panel-mask');
			if (!m.length){
				m = $('<div class="panel-mask"></div>').appendTo(pal);
			}
			m.css({
				background:'#fff',
				left:borderSize,
				top:(borderSize+pal.children('.panel-header')._outerHeight()),
				right:borderSize,
				bottom:borderSize
			});
			m.children('div.panel-mask-msg').remove();
			var mm = $('<div class="panel-mask-msg"></div>').appendTo(m);
			mm.html(msg).css({position:'absolute'}).css({
				position:'absolute',
				top: '50%',
				left: '50%',
				marginTop: -mm._outerHeight()/2,
				marginLeft: -mm._outerWidth()/2
			})
		});
	},
	hideMask: function(jq){
		return jq.each(function(){
			$(this).panel('panel').children('div.panel-mask').remove();
		})
	}
});
$.extend($.fn.validatebox.defaults.rules,{
    inList:{
           validator:function(value,param){
                  var c = $(param[0]);
                  var opts = c.combobox('options');
                  var data = c.combobox('getData');
                  var exists = false;
                  for(var i=0; i<data.length; i++){
                         if (value == data[i][opts.textField]){
                                exists = true;
                                break;
                         }
                  }
                  return exists;
           },
           message:'invalid value.'
    }
})

function paketTindakan(lis){
    var paket={}
    paket['csrfmiddlewaretoken']=getCookie('csrftoken');
    for (i=0;i<lis.length;i++){
        paket[lis[i]]=lis[i];
    }
    $.ajax({
        type: "POST",
        url: "{% url 'paketTarif' %}",
        data: paket,
        success: function(data){
            console.log( data );
        },
    });
}
function terbilang(bilangan) {

    bilangan    = String(bilangan);
    var angka   = new Array('0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0');
    var kata    = new Array('','Satu','Dua','Tiga','Empat','Lima','Enam','Tujuh','Delapan','Sembilan');
    var tingkat = new Array('','Ribu','Juta','Milyar','Triliun');
   
    var panjang_bilangan = bilangan.length;
   
    /* pengujian panjang bilangan */
    if (panjang_bilangan > 15) {
      kaLimat = "Diluar Batas";
      return kaLimat;
    }
   
    /* mengambil angka-angka yang ada dalam bilangan, dimasukkan ke dalam array */
    for (i = 1; i <= panjang_bilangan; i++) {
      angka[i] = bilangan.substr(-(i),1);
    }
   
    i = 1;
    j = 0;
    kaLimat = "";
   
   
    /* mulai proses iterasi terhadap array angka */
    while (i <= panjang_bilangan) {
   
      subkaLimat = "";
      kata1 = "";
      kata2 = "";
      kata3 = "";
   
      /* untuk Ratusan */
      if (angka[i+2] != "0") {
        if (angka[i+2] == "1") {
          kata1 = "Seratus";
        } else {
          kata1 = kata[angka[i+2]] + " Ratus";
        }
      }
   
      /* untuk Puluhan atau Belasan */
      if (angka[i+1] != "0") {
        if (angka[i+1] == "1") {
          if (angka[i] == "0") {
            kata2 = "Sepuluh";
          } else if (angka[i] == "1") {
            kata2 = "Sebelas";
          } else {
            kata2 = kata[angka[i]] + " Belas";
          }
        } else {
          kata2 = kata[angka[i+1]] + " Puluh";
        }
      }
   
      /* untuk Satuan */
      if (angka[i] != "0") {
        if (angka[i+1] != "1") {
          kata3 = kata[angka[i]];
        }
      }
   
      /* pengujian angka apakah tidak nol semua, lalu ditambahkan tingkat */
      if ((angka[i] != "0") || (angka[i+1] != "0") || (angka[i+2] != "0")) {
        subkaLimat = kata1+" "+kata2+" "+kata3+" "+tingkat[j]+" ";
      }
   
      /* gabungkan variabe sub kaLimat (untuk Satu blok 3 angka) ke variabel kaLimat */
      kaLimat = subkaLimat + kaLimat;
      i = i + 3;
      j = j + 1;
   
    }
   
    /* mengganti Satu Ribu jadi Seribu jika diperlukan */
    if ((angka[5] == "0") && (angka[6] == "0")) {
      kaLimat = kaLimat.replace("Satu Ribu","Seribu");
    }
   
    return kaLimat + "Rupiah";
   }