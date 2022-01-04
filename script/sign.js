// 全局不参与签名
const ignores = ['t'];

// 签名加密参数
const appKey = '00000001';
const secretKey = '52c203760cf28798a44f6ac4';
const format = 'json';
const version = '1.0';
const hexcase = 0;

function createSign(params) {
  const keys = Object.keys(params);
  const hashMap = [];

  keys.forEach(key => {
    hashMap.push({
      key,
      value: params[key]
    });
  });
  hashMap.sort(orderBy('key'));

  return ropsign(hashMap, secretKey);
}

function orderBy(name) {
  return function (o, p) {
    var a, b;
    if (typeof o === 'object' && typeof p === 'object' && o && p) {
      a = o[name];
      b = p[name];
      if (a === b) {
        return 0;
      }
      if (typeof a === typeof b) {
        return a < b ? -1 : 1;
      }
      return typeof a < typeof b ? -1 : 1;
    } else {
      throw new Error('error');
    }
  };
}

function ropsign(arrtest, secretKey) {
  var sss = '';
  sss = sss + secretKey;
  for (var key = 0; key < arrtest.length; key++) {
    sss = sss + arrtest[key].key + arrtest[key].value;
  }
  sss = sss + secretKey;
  return hex_sha1(utf16to8(sss));
}

function utf16to8(str) {
  var out, i, len, c;

  out = '';
  len = str.length;
  for (i = 0; i < len; i++) {
    c = str.charCodeAt(i);
    if (c >= 0x0001 && c <= 0x007f) {
      out += str.charAt(i);
    } else if (c > 0x07ff) {
      out += String.fromCharCode(0xe0 | ((c >> 12) & 0x0f));
      out += String.fromCharCode(0x80 | ((c >> 6) & 0x3f));
      out += String.fromCharCode(0x80 | ((c >> 0) & 0x3f));
    } else {
      out += String.fromCharCode(0xc0 | ((c >> 6) & 0x1f));
      out += String.fromCharCode(0x80 | ((c >> 0) & 0x3f));
    }
  }

  return out;
}

/* eslint-disable */
function hex_sha1(s) {
  return binb2hex(core_sha1(alignSHA1(s)));
}

function alignSHA1(str) {
  var nblk = ((str.length + 8) >> 6) + 1;

  var blks = new Array(nblk * 16);
  for (var i = 0; i < nblk * 16; i++) blks[i] = 0;
  for (i = 0; i < str.length; i++) { blks[i >> 2] |= str.charCodeAt(i) << (24 - (i & 3) * 8); }
  blks[i >> 2] |= 0x80 << (24 - (i & 3) * 8);
  blks[nblk * 16 - 1] = str.length * 8;
  return blks;
}

function core_sha1(blockArray) {
  var x = blockArray; // append padding
  var w = Array(80);
  var a = 1732584193;
  var b = -271733879;
  var c = -1732584194;
  var d = 271733878;
  var e = -1009589776;
  for (
    var i = 0;
    i < x.length;
    i += 16 // 每次处理512位 16*32
  ) {
    var olda = a;
    var oldb = b;
    var oldc = c;
    var oldd = d;
    var olde = e;
    for (
      var j = 0;
      j < 80;
      j++ // 对每个512位进行80步操作
    ) {
      if (j < 16) w[j] = x[i + j];
      else w[j] = rol(w[j - 3] ^ w[j - 8] ^ w[j - 14] ^ w[j - 16], 1);
      var t = safe_add(
        safe_add(rol(a, 5), sha1_ft(j, b, c, d)),
        safe_add(safe_add(e, w[j]), sha1_kt(j))
      );
      e = d;
      d = c;
      c = rol(b, 30);
      b = a;
      a = t;
    }
    a = safe_add(a, olda);
    b = safe_add(b, oldb);
    c = safe_add(c, oldc);
    d = safe_add(d, oldd);
    e = safe_add(e, olde);
  }
  return [a, b, c, d, e];
}

function rol(num, cnt) {
  return (num << cnt) | (num >>> (32 - cnt));
}

function sha1_kt(t) {
  return t < 20
    ? 1518500249
    : t < 40
      ? 1859775393
      : t < 60
        ? -1894007588
        : -899497514;
}

function sha1_ft(t, b, c, d) {
  if (t < 20) return (b & c) | (~b & d);

  if (t < 40) return b ^ c ^ d;

  if (t < 60) return (b & c) | (b & d) | (c & d);
  return b ^ c ^ d; // t<80
}

function safe_add(x, y) {
  var lsw = (x & 0xffff) + (y & 0xffff);
  var msw = (x >> 16) + (y >> 16) + (lsw >> 16);
  return (msw << 16) | (lsw & 0xffff);
}

function binb2hex(binarray) {
  var hex_tab = hexcase ? '0123456789ABCDEF' : '0123456789abcdef';
  var str = '';
  for (var i = 0; i < binarray.length * 4; i++) {
    str +=
      hex_tab.charAt((binarray[i >> 2] >> ((3 - (i % 4)) * 8 + 4)) & 0xf) +
      hex_tab.charAt((binarray[i >> 2] >> ((3 - (i % 4)) * 8)) & 0xf);
  }
  return str.toUpperCase();
}