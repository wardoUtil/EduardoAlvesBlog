var PostView = Backbone.View.extend({
    model: new Post(),
    tagName: 'div',
    initialize: function() {
        this.template = _.template($('#post-template').html());
    },
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

var PostsView = Backbone.View.extend({
    model: posts,
    el: $('#posts-container'),
    initialize: function(){
        this.model.on('add', this.render, this);
    },
    render: function(){
        var self = this;
        self.$el.html('');
        _.each(this.model.toArray(), function(post, i){
            self.$el.append((new PostView({model:post})).render().$el);
        });
        return this;
    }
});

var postsView = new PostsView();


var CommentView = Backbone.View.extend({
    model: new Comment(),
    tagName: 'div',
    initialize: function() {
        this.template = _.template($('#comment-template').html());
    },
    render: function() {
        this.$el.html(this.template(this.model.toJSON()));
        return this;
    }
});

var CommentsView = Backbone.View.extend({
    model: comments,
    el: $('#comments'),
    initialize: function(){
        this.model.on('add', this.render, this);
    },
    render: function(){
        var self = this;
        self.$el.html('');
        _.each(this.model.toArray(), function(comment, i){
            self.$el.append((new CommentView({model:comment})).render().$el);
        });
        return this;
    }
});

var commentsView = new CommentsView();
