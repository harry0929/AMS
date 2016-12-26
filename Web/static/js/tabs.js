
/**
 * Created by zhaoquanzhi on 16/4/23
 * JSON无限折叠菜单
 */


function getOuterWidth(n){
    var k = 0;
        $(n).each(function () {
            k += $(this).outerWidth(true);
        });
        return k
}

//添加Tab
function appendTab() {
    var url = $(this).attr("data-url"),
        id = $(this).attr("data-id"),
        title = $.trim($(this).text()),
        flag = true;
    if(url == "#" || url == "" || url == undefined)
        return false;

    //判断是否存在该标签
    $(".tabs-menu").each(function () {
            if ($(this).data("id") == id) {
                if (!$(this).hasClass("active")) {
                    $(this).addClass("active").siblings(".tabs-menu").removeClass("active");
                    //g(this);
                    $(".tabs-frame").each(function () {
                        if ($(this).data("id") == id) {
                            $(this).show().siblings(".tabs-frame").hide();
                            return false;
                        }
                    })
                }
                flag = false;
                return false;
            }
        });
    //添加新节点
    if(flag) {
        $(".tabs-menu").removeClass("active");
        var p = '<a href="#" class="tabs-menu active" data-id="' + id + '">' + title + '<i class="fa fa-times-circle"></i></a>';
        $(".tabs-menus").append(p);
        var n = '<iframe class="tabs-frame" data-id="' + id + '" name="iframe' + id + '" width="100%" height="100%" src="' + url + '" frameborder="0 seamless=""></iframe>'
        $(".tabs-frame").hide().parents(".tabs-frames").append(n);
    }
}
//关闭所有tab
function closeAllTabs() {
    $(".tabs-menu").nextAll().remove();
    $(".tabs-frame").nextAll().remove();

    showLastTab();
}

//关闭tab
function closeTab() {
    $(this).parent(".tabs-menu").remove();
    $(".tabs-frame[name=iframe" + $(this).parent(".tabs-menu").attr("data-id") + "]").remove();
    showLastTab();
}
//关闭其他
function closeOtherTab() {
    $(".tabs-menu").nextAll().not(".active").each(function () {
        $(".tabs-frame[name=iframe" + $(this).attr("data-id") + "]").remove();
        $(this).remove();
    });
}

//显示tab
function showLastTab() {
    $(".tabs-menu").last().addClass("active");
    $(".tabs-frame").last().show();
}

function activeTab() {
    $(this).addClass("active").siblings(".tabs-menu").removeClass("active");
    //$(".tabs-frame").hide();
    $(".tabs-frame[name=iframe" + $(this).attr("data-id") + "]").show().siblings(".tabs-frame").hide();
}



function rollLeftTab(n)
{
    var o = getOuterWidth($(".tabs-menu.active").prevAll()),
        q = getOuterWidth($(".tabs-menu.active").nextAll());

    alert(o);

    var l = getOuterWidth($(".tabs-container").children().not(".tabs-menus"));
    var k = $(".tabs-container").outerWidth(true) - l;
    var wMenus = $(".tabs-menus").outerWidth();
    alert(wMenus);
    if (wMenus < k)
    {
        alert("lt");
    }
    else
    {
        alert("lg");
    }
}


$(function(){
    //添加tab
    $(".menu").on("click", appendTab);
    $(".tabs-menus").on("click", ".tabs-menu i", closeTab)
    $(".tabs-close-all").on("click",closeAllTabs)
    $(".tabs-close-other").on("click", closeOtherTab);
    $(".tabs-menus").on("click", "a", activeTab);

    $(".roll-left").on("click",rollLeftTab);

    //初始化菜单
    $.post("/home/getMenus",function(ret){
            new AccordionMenu({menuArrs:eval(ret)});
            $('#sidebar-menus').metisMenu();
        });

});


function AccordionMenu(options) {
    this.config = {
        containerCls: '.wrapper-nav',                // 外层容器
        menuArrs: '',                         //  JSON传进来的数据
        renderCallBack: null,                       // 渲染html结构后回调
        clickItemCallBack: null                         // 每点击某一项时候回调
    };
    this.cache = {};
    this.init(options);
}



AccordionMenu.prototype = {
    constructor: AccordionMenu,
    init: function (options) {
        this.config = $.extend(this.config, options || {});
        var self = this,
            _config = self.config,
            _cache = self.cache;

        // 渲染html结构
        $(_config.containerCls).each(function (index, item) {

            self._renderHTML(item);
        });
    },
    _renderHTML: function (container) {
        var self = this,
            _config = self.config,
            _cache = self.cache;
        var ulhtml = $('<ul class="nav metismenu" id="sidebar-menus">');
        $(_config.menuArrs).each(function (index, item) {
            var lihtml = $('<li><a href="#"><i class="fa fa-th-larg"></i><span class="nav-label">' + item.name + '</span></a></li>');
            if (item.submenu && item.submenu.length > 0) {
                $(lihtml).find('a').append('<span class="fa arrow"></span>');
                self._createSubMenu(item.submenu, lihtml);
            }
            else {
                $(lihtml).find('a').attr("data-id", item.id);
                $(lihtml).find('a').attr("data-url", item.url);
                $(lihtml).find('a').on("click", appendTab);

            }
            $(ulhtml).append(lihtml);
        });
        $(container).append(ulhtml);

        _config.renderCallBack && $.isFunction(_config.renderCallBack) && _config.renderCallBack();

    },
    /**
     * 创建子菜单
     * @param {array} 子菜单
     * @param {lihtml} li项
     */
    _createSubMenu: function (submenu, lihtml) {
        var self = this,
            _config = self.config,
            _cache = self.cache;
        var subUl = $('<ul class="nav nav-sub-level"><ul>'),
            callee = arguments.callee,
            subLi;

        $(submenu).each(function (index, item) {
            //var url = item.url || 'javascript:void(0)';

            //<li ><a href="{{ sub.url }}">{{ sub.name }}</a></li>

            subLi = $('<li><a href="#">' + item.name + '</a></li>');
            if (item.submenu && item.submenu.length > 0) {
                //$(subLi).children('a').prepend('<img src="images/blank.gif" alt=""/>');
                _createSubMenu(item.submenu, subLi);
            }
            else {
                $(subLi).find('a').attr("data-id", item.id);
                $(subLi).find('a').attr("data-url", item.url);
                $(subLi).find('a').on("click", appendTab);

            }
            $(subUl).append(subLi);
        });
        $(lihtml).append(subUl);
    }
};