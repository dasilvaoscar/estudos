"use strict";

function _typeof(obj) { "@babel/helpers - typeof"; if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); return Constructor; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function"); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, writable: true, configurable: true } }); if (superClass) _setPrototypeOf(subClass, superClass); }

function _setPrototypeOf(o, p) { _setPrototypeOf = Object.setPrototypeOf || function _setPrototypeOf(o, p) { o.__proto__ = p; return o; }; return _setPrototypeOf(o, p); }

function _createSuper(Derived) { var hasNativeReflectConstruct = _isNativeReflectConstruct(); return function _createSuperInternal() { var Super = _getPrototypeOf(Derived), result; if (hasNativeReflectConstruct) { var NewTarget = _getPrototypeOf(this).constructor; result = Reflect.construct(Super, arguments, NewTarget); } else { result = Super.apply(this, arguments); } return _possibleConstructorReturn(this, result); }; }

function _possibleConstructorReturn(self, call) { if (call && (_typeof(call) === "object" || typeof call === "function")) { return call; } return _assertThisInitialized(self); }

function _assertThisInitialized(self) { if (self === void 0) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return self; }

function _isNativeReflectConstruct() { if (typeof Reflect === "undefined" || !Reflect.construct) return false; if (Reflect.construct.sham) return false; if (typeof Proxy === "function") return true; try { Date.prototype.toString.call(Reflect.construct(Date, [], function () {})); return true; } catch (e) { return false; } }

function _getPrototypeOf(o) { _getPrototypeOf = Object.setPrototypeOf ? Object.getPrototypeOf : function _getPrototypeOf(o) { return o.__proto__ || Object.getPrototypeOf(o); }; return _getPrototypeOf(o); }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

var Model = function Model() {
  _classCallCheck(this, Model);

  this.title = [];
  this.desc = [];
};

var Controller = /*#__PURE__*/function (_Model) {
  _inherits(Controller, _Model);

  var _super = _createSuper(Controller);

  function Controller() {
    _classCallCheck(this, Controller);

    return _super.call(this);
  }

  _createClass(Controller, [{
    key: "getTitle",
    value: function getTitle() {
      return this.title;
    }
  }, {
    key: "setTitle",
    value: function setTitle(title) {
      this.title.push(title);
      console.log(this.title);
    }
  }, {
    key: "getDesc",
    value: function getDesc() {
      return this.desc;
    }
  }, {
    key: "setDesc",
    value: function setDesc(desc) {
      this.desc.push(desc);
      console.log(this.desc);
    }
  }]);

  return Controller;
}(Model);

var Interface = /*#__PURE__*/function (_Controller) {
  _inherits(Interface, _Controller);

  var _super2 = _createSuper(Interface);

  function Interface() {
    _classCallCheck(this, Interface);

    return _super2.call(this);
  }

  _createClass(Interface, [{
    key: "insertCard",
    value: function insertCard(title, desc) {
      debugger;
      var container = document.querySelector('.container');
      var card = document.createElement('div');
      var img = document.createElement('img');
      var card_body = document.createElement('div');
      var h5 = document.createElement('h5');
      var p = document.createElement('p');
      var a = document.createElement('a');
      var detail = document.createTextNode('Detalhes');
      var node_title = document.createTextNode(title);
      var node_desc = document.createTextNode(desc);
      container.appendChild(card);
      card.appendChild(img);
      card.appendChild(card_body);
      card_body.appendChild(h5);
      card_body.appendChild(p);
      card_body.appendChild(a);
      card.setAttribute('class', 'card');
      img.setAttribute('src', 'https://png.pngtree.com/png-vector/20190411/ourlarge/pngtree-vector-html-icon-png-image_925883.jpg');
      img.setAttribute('class', 'card-img-top');
      img.setAttribute('alt', '...');
      card_body.setAttribute('class', 'card-body');
      h5.setAttribute('class', 'card-title');
      h5.appendChild(node_title);
      p.setAttribute('class', 'card-text');
      p.appendChild(node_desc);
      a.setAttribute('href', '#');
      a.setAttribute('class', 'btn btn-primary');
      a.appendChild(detail);
    }
  }]);

  return Interface;
}(Controller);

var ControllerList = new Controller();
var InterfaceList = new Interface();
var ModelList = new Model();

document.getElementById('novotodo').onclick = function () {
  ControllerList.setTitle(document.getElementById('title').value);
  ControllerList.setDesc(document.getElementById('desc').value);
  InterfaceList.insertCard(ControllerList.title, ControllerList.desc);
};
