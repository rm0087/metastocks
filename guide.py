class Artist(db.Model, SerializerMixin):
    
    
    # define a table name

    
    # arg 1 = type of value
    # arg x = primary_key=, nullable=, etc.

    # arg 1 = name of the other class
    # arg 2 = back populates => the name of the method in the other class pointing to this class
    # arg 3 = deletes albums for artist when artist is deleted

    # arg 1 = relatiionship name we're going through
    # arg 2 = the relationship that brings us to our final destination

    ## use SerializerMixin to filter out related attributes from other classes to avoid infinite loops

    #### TO SET-UP TABLES ####
        ## flask db init
        ## flask db migrate -m "message here"
        ## flask db upgrade

    ## flask shell
    ## >> db.session.add(variable_to_add)
    ## >> db.session.add_all([x1, x2, x3]) ## add multiple variables in list form