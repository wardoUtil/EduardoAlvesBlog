/**
 * Created by Eduardo on 07-09-2014.
 */
var Post = Backbone.Model.extend({
    defaults: function() {
       return {
        title: 'How To Hire A Designer',
        text: '',
        shares: 17,
        comments: 13,
        url: '/',
        date : {
            day: 5,
            month: 'October'
        }
    }
    }
});

var Comment = Backbone.Model.extend({
    defaults: function(){
    return {
        picture: 'file:///C:/Users/Eduardo/PycharmProjects/Entrepreneur%20Blog/img/profile_pic.png',
        name: '',
        text: '',
        date: {
            day: 1,
            month: 'October',
            year: 2015
        }
    }
}
});
/**
var ResponseComment = Backbone.Model.extend({
        defaults: function(){
        return {
        picture: '',
        name: '',
        text: '',
        date: {
            day: 1,
            month: 'October',
            year: 2015
        }
        }
        }
});
*/
var Comments = Backbone.Collection.extend({
    model: Comment
});

var Posts = Backbone.Collection.extend({
    model: Post
});

posts = new Posts();
comments = new Comments();

console.log(posts.toJSON());