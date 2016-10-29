# connect to localhost development database
# CONNECT remote:/development admin admin

BEGIN
# create UserAccount class
CREATE CLASS User extends V

CREATE PROPERTY User.email         STRING
CREATE PROPERTY User.created_on    DATETIME
CREATE PROPERTY User.display_name  STRING
CREATE PROPERTY User.profile_photo STRING
CREATE PROPERTY User.status        STRING
CREATE PROPERTY User.role          STRING
# CREATE PROPERTY Profile.features      SHORT
CREATE PROPERTY User.genres        LINKSET
CREATE PROPERTY User.deleted_at    DATETIME

## Edges
CREATE PROPERTY User.in_BelongsTo  LINKBAG
CREATE PROPERTY User.out_Has       LINKBAG
CREATE PROPERTY User.out_Manage    LINKBAG
CREATE PROPERTY User.out_Follow    LINKBAG
CREATE PROPERTY User.out_Converse  LINKBAG
CREATE PROPERTY User.out_Reject    LINKBAG
CREATE PROPERTY User.out_Creates   LINKBAG
CREATE PROPERTY User.out_Changes   LINKBAG

ALTER PROPERTY User.email      MANDATORY true
ALTER PROPERTY User.created_on MANDATORY true
ALTER PROPERTY User.status     MANDATORY true
# ALTER PROPERTY Profile.features   MANDATORY true

ALTER PROPERTY User.created_on DEFAULT sysdate() READONLY
ALTER PROPERTY User.status     DEFAULT "unverified"
# user for normal bookya user -- user
# admin for bookya admin -- user + admin
# su for super user -- meaning can do all admin and user restricted features
ALTER PROPERTY User.role       REGEXP  user|admin|su

CREATE INDEX   User.email    UNIQUE_HASH_INDEX

ALTER CLASS User STRICTMODE true
# end create UserAccount class

# create Social Proof class
CREATE CLASS Identity extends V

CREATE PROPERTY Identity.type            STRING
CREATE PROPERTY Identity.key             STRING
CREATE PROPERTY Identity.id              STRING
CREATE PROPERTY Identity.token           STRING
CREATE PROPERTY Identity.created_on      DATETIME
CREATE PROPERTY Identity.raw             EMBEDDED
CREATE PROPERTY Identity.allowed_devices LINKSET

## Edges
CREATE PROPERTY Identity.in_Has          LINKBAG

ALTER PROPERTY Identity.type  MANDATORY true
ALTER PROPERTY Identity.token MANDATORY true
ALTER PROPERTY Identity.type  REGEXP    email|facebook|soundcloud|twitter|linkedin

ALTER PROPERTY Identity.created_on DEFAULT sysdate() readonly

CREATE INDEX SP_UniqueSocialAccount ON Identity(type, key, token) UNIQUE_HASH_INDEX

ALTER CLASS Identity STRICTMODE true
# end create Social Proof class

# create Artist class
CREATE CLASS Artist extends V

CREATE PROPERTY Artist.full_name       STRING
CREATE PROPERTY Artist.display_name    STRING
CREATE PROPERTY Artist.email           STRING
CREATE PROPERTY Artist.manager_email   STRING
CREATE PROPERTY Artist.management      STRING
CREATE PROPERTY Artist.nationality     STRING
CREATE PROPERTY Artist.territories     STRING
CREATE PROPERTY Artist.contact_number  STRING
CREATE PROPERTY Artist.created_on      DATETIME
CREATE PROPERTY Artist.artist_bio      STRING
CREATE PROPERTY Artist.bookya_url      STRING
CREATE PROPERTY Artist.media_list      LINKSET
CREATE PROPERTY Artist.milestone_list  EMBEDDEDLIST
CREATE PROPERTY Artist.profession_list LINKSET
CREATE PROPERTY Artist.genre_list      LINKSET
CREATE PROPERTY Artist.website_list    EMBEDDEDSET
CREATE PROPERTY Artist.cover_photo     LINK
CREATE PROPERTY Artist.profile_photo   LINK
# list of postgresql id, for country
CREATE PROPERTY Artist.based_in        EMBEDDEDSET
CREATE PROPERTY Artist.featured_track  STRING
CREATE PROPERTY Artist.record_labels   EMBEDDEDSET
CREATE PROPERTY Artist.agent_list      LINKSET
CREATE PROPERTY Artist.other_names     EMBEDDEDSET
CREATE PROPERTY Artist.email_verified  BOOLEAN

## Edges
CREATE PROPERTY Artist.in_Manage       LINKBAG
CREATE PROPERTY Artist.in_Follow       LINKBAG
CREATE PROPERTY Artist.out_PerformedAt LINKBAG
CREATE PROPERTY Artist.out_Own         LINKBAG
CREATE PROPERTY Artist.in_Reject       LINKBAG
CREATE PROPERTY Artist.in_Converse     LINKBAG
CREATE PROPERTY Artist.in_For          LINKBAG

ALTER PROPERTY Artist.display_name MANDATORY true
ALTER PROPERTY Artist.full_name    MANDATORY true

ALTER PROPERTY Artist.created_on     DEFAULT sysdate() readonly
ALTER PROPERTY Artist.email_verified DEFAULT false

CREATE INDEX Artist.bookya_url    UNIQUE_HASH_INDEX
CREATE INDEX Artist.display_name  FULLTEXT
CREATE INDEX Artist.full_name     FULLTEXT

ALTER CLASS Artist STRICTMODE true
# end of create Artist class

# create promoter class
# Promoter might be a person or a company
CREATE CLASS Promoter extends V

CREATE PROPERTY Promoter.full_name       STRING
# possibly person name or company name
CREATE PROPERTY Promoter.display_name    STRING
CREATE PROPERTY Promoter.email           STRING
CREATE PROPERTY Promoter.contact_number  STRING
CREATE PROPERTY Promoter.created_on      DATETIME
CREATE PROPERTY Promoter.bio             STRING
CREATE PROPERTY Promoter.bookya_url      STRING
CREATE PROPERTY Promoter.genre_list      LINKSET
CREATE PROPERTY Promoter.website_list    EMBEDDEDSET
CREATE PROPERTY Promoter.cover_photo     LINK
CREATE PROPERTY Promoter.profile_photo   LINK
CREATE PROPERTY Promoter.email_verified  BOOLEAN

# list of postgresql id, for country
CREATE PROPERTY Promoter.based_in        EMBEDDEDSET
# event information for each promoter
CREATE PROPERTY Promoter.event_location_list EMBEDDEDSET
CREATE PROPERTY Promoter.event_type_list     LINKSET
CREATE PROPERTY Promoter.significant_booking_list  EMBEDDEDSET
CREATE PROPERTY Promoter.concept_list              EMBEDDEDSET

CREATE PROPERTY Promoter.out_Own         LINKBAG
CREATE PROPERTY Promoter.in_Manage       LINKBAG
CREATE PROPERTY Promoter.in_Follow       LINKBAG
CREATE PROPERTY Promoter.in_Converse     LINKBAG
CREATE PROPERTY Promoter.in_With         LINKBAG
CREATE PROPERTY Promoter.in_Reject       LINKBAG

ALTER PROPERTY Promoter.display_name MANDATORY true
ALTER PROPERTY Promoter.full_name    MANDATORY true

ALTER PROPERTY Promoter.created_on     DEFAULT sysdate() readonly
ALTER PROPERTY Promoter.email_verified DEFAULT false

CREATE INDEX Promoter.bookya_url    UNIQUE_HASH_INDEX
CREATE INDEX Promoter.display_name  FULLTEXT
CREATE INDEX Promoter.full_name     FULLTEXT

ALTER CLASS Promoter STRICTMODE true
# end create promoter class

# create agency class
CREATE CLASS Agency extends V

CREATE PROPERTY Agency.name        STRING
CREATE PROPERTY Agency.agent       STRING
CREATE PROPERTY Agency.email       STRING
CREATE PROPERTY Agency.number      STRING
CREATE PROPERTY Agency.territories STRING

ALTER CLASS Agency STRICTMODE true
# end of create agency class

# create Show class
CREATE CLASS Show extends V

CREATE PROPERTY Show.type         EMBEDDEDSET
CREATE PROPERTY Show.start_date   DATETIME
CREATE PROPERTY Show.end_date     DATETIME
CREATE PROPERTY Show.name         STRING
CREATE PROPERTY Show.slug         STRING
CREATE PROPERTY Show.description  STRING
CREATE PROPERTY Show.lineup_listing STRING
CREATE PROPERTY Show.cover_img    STRING
CREATE PROPERTY Show.social_proof LINK
CREATE PROPERTY Show.state        STRING
CREATE PROPERTY Show.ticket_url   STRING
CREATE PROPERTY Show.ticket_price DOUBLE
CREATE PROPERTY Show.ticket_currency STRING
CREATE PROPERTY Show.created_on   DATETIME
CREATE PROPERTY Show.held_at      INTEGER
## external id to track which social site we are using it from
CREATE PROPERTY Show.id           STRING
## Edges
CREATE PROPERTY Show.out_At         LINKBAG
CREATE PROPERTY Show.in_PerformedAt LINKBAG
CREATE PROPERTY Show.in_Organized   LINKBAG
CREATE PROPERTY Show.in_In          LINKBAG

# enum
ALTER PROPERTY Show.state REGEXP draft|public|published
ALTER PROPERTY Show.state DEFAULT "draft"

ALTER PROPERTY Show.name  MANDATORY true
ALTER PROPERTY Show.state MANDATORY true

ALTER PROPERTY Show.created_on DEFAULT sysdate() readonly

CREATE INDEX Show.slug        UNIQUE_HASH_INDEX
CREATE INDEX Show.name        FULLTEXT
CREATE INDEX Show.description FULLTEXT

ALTER CLASS Show STRICTMODE true
# end create Show class

# create Social Metric class
CREATE CLASS SocialMetric extends V

CREATE PROPERTY SocialMetric.type   STRING
CREATE PROPERTY SocialMetric.id     STRING
CREATE PROPERTY SocialMetric.value  DOUBLE
CREATE PROPERTY SocialMetric.token  STRING
CREATE PROPERTY SocialMetric.others EMBEDDED

## Edges
CREATE PROPERTY SocialMetric.in_Own LINKBAG

ALTER PROPERTY SocialMetric.type  MANDATORY true
ALTER PROPERTY SocialMetric.id    MANDATORY true

CREATE INDEX SM_UniqueSocialAccount ON SocialMetric(type, id) UNIQUE_HASH_INDEX

ALTER CLASS SocialMetric STRICTMODE true
# end create Social Metric class

# create Genre class
CREATE CLASS Genre extends V

CREATE PROPERTY Genre.value      STRING
CREATE PROPERTY Genre.created_by LINK

ALTER PROPERTY Genre.value MANDATORY true

CREATE INDEX Genre.value FULLTEXT

ALTER CLASS Genre STRICTMODE true
# end of create Genre class

# create Profession class
CREATE CLASS Profession extends V

CREATE PROPERTY Profession.value      STRING
CREATE PROPERTY Profession.created_by LINK

ALTER PROPERTY Profession.value MANDATORY true

CREATE INDEX Profession.value UNIQUE_HASH_INDEX

ALTER CLASS Profession STRICTMODE true
# end of create Profession class

# create Media class
CREATE CLASS Media extends V

CREATE PROPERTY Media.value      STRING
CREATE PROPERTY Media.type       STRING
CREATE PROPERTY Media.created_by LINK

ALTER PROPERTY Media.value MANDATORY true
ALTER PROPERTY Media.type  MANDATORY true

ALTER PROPERTY Media.created_by LINKEDCLASS user
ALTER PROPERTY Media.type  REGEXP    cover|profile|gallery|music|video

CREATE INDEX Media_UniqueTypeValue ON Media(value, type) UNIQUE_HASH_INDEX

ALTER CLASS Media STRICTMODE true
# end create Media class

# create Article class
CREATE CLASS Article extends V

CREATE PROPERTY Article.url          STRING
CREATE PROPERTY Article.description  STRING
CREATE PROPERTY Article.title        STRING
CREATE PROPERTY Article.image        STRING
CREATE PROPERTY Article.tags         EMBEDDEDSET

ALTER PROPERTY Article.url MANDATORY true

ALTER CLASS Article STRICTMODE true
# end create Article class

# create Message class
CREATE CLASS Message extends V

CREATE PROPERTY Message.message      STRING
CREATE PROPERTY Message.owner        LINK
CREATE PROPERTY Message.conversation LINK
CREATE PROPERTY Message.created_on   DATETIME

ALTER PROPERTY Message.created_on   DEFAULT sysdate() readonly
ALTER PROPERTY Message.conversation MANDATORY true
ALTER PROPERTY Message.owner        MANDATORY true
ALTER PROPERTY Message.message      MANDATORY true

ALTER CLASS Message STRICTMODE true
# end create Message class

# creates a Device class that is reponsible for documenting all devices and their notification tokens
CREATE CLASS Device extends V

CREATE PROPERTY Device.device_id            STRING
CREATE PROPERTY Device.notifications_token  STRING
CREATE PROPERTY Device.type                 STRING
CREATE PROPERTY Device.login                BOOLEAN
CREATE PROPERTY Device.profile              LINK

ALTER PROPERTY Device.device_id MANDATORY true
ALTER PROPERTY Device.login     DEFAULT true
# enums for device type platform
ALTER PROPERTY Device.type      REGEXP  ios|android|web

ALTER CLASS Device STRICTMODE true

# create Notification class, that correspond to notifications send to users
CREATE CLASS Notification extends V

CREATE PROPERTY Notification.label          STRING
CREATE PROPERTY Notification.message        STRING
CREATE PROPERTY Notification.created_on     DATETIME
CREATE PROPERTY Notification.action_type    STRING
CREATE PROPERTY Notification.data           STRING
CREATE PROPERTY Notification.version        STRING
CREATE PROPERTY Notification.related        LINK

CREATE PROPERTY Notification.out_BelongsTo  LINKBAG

ALTER PROPERTY Notification.label        MANDATORY true
ALTER PROPERTY Notification.message      MANDATORY true
ALTER PROPERTY Notification.created_on   DEFAULT sysdate() readonly
ALTER PROPERTY Notification.version      DEFAULT "1.3"
# enums for device type platform
ALTER PROPERTY Notification.action_type  REGEXP  NOTIFICATIONS|ARTIST|CLAIM_SOCIALS|BOOKING_REQUEST|PROMOTER

ALTER CLASS Notification STRICTMODE true

# booking class
CREATE CLASS BookingRequest extends V

CREATE PROPERTY BookingRequest.message       STRING
# psql location id
CREATE PROPERTY BookingRequest.negotiable  BOOLEAN
CREATE PROPERTY BookingRequest.price         FLOAT
# possibly putting this to a separate table
CREATE PROPERTY BookingRequest.currency      STRING
CREATE PROPERTY BookingRequest.status        STRING
CREATE PROPERTY BookingRequest.created_on    DATETIME
# edges
CREATE PROPERTY BookingRequest.out_For       LINKBAG
CREATE PROPERTY BookingRequest.out_With      LINKBAG
# booking request in event
CREATE PROPERTY BookingRequest.out_In        LINKBAG
CREATE PROPERTY BookingRequest.in_Creates    LINKBAG
CREATE PROPERTY BookingRequest.in_Changes    LINKBAG

ALTER PROPERTY BookingRequest.created_on   DEFAULT sysdate() readonly
ALTER PROPERTY BookingRequest.negotiable   DEFAULT true
ALTER PROPERTY BookingRequest.price        DEFAULT 0.00
ALTER PROPERTY BookingRequest.status       DEFAULT "pending"

ALTER PROPERTY BookingRequest.status       REGEXP  pending|accept|reject|confirm|cancel

ALTER CLASS BookingRequest STRICTMODE true

# Venue Profile class
CREATE CLASS Venue extends V

CREATE PROPERTY Venue.name        STRING
CREATE PROPERTY Venue.description STRING
CREATE PROPERTY Venue.bookya_url  STRING
CREATE PROPERTY Venue.external_id STRING
CREATE PROPERTY Venue.capacity    INTEGER
CREATE PROPERTY Venue.website     STRING
Create PROPERTY Venue.location_id INTEGER

CREATE PROPERTY Venue.in_Manage  LINKBAG
CREATE PROPERTY Venue.in_At      LINKBAG

ALTER PROPERTY Venue.name         MANDATORY true
ALTER PROPERTY Venue.location_id  MANDATORY true

ALTER CLASS Venue STRICTMODE true

# Event type
CREATE CLASS EventType extends V

CREATE PROPERTY EventType.value      STRING
CREATE PROPERTY EventType.created_on DATETIME

ALTER PROPERTY EventType.value      MANDATORY true
ALTER PROPERTY EventType.created_on DEFAULT sysdate() readonly

CREATE INDEX EventType.value UNIQUE_HASH_INDEX

ALTER CLASS EventType STRICTMODE true
## end of create eventtype class

## Account has many identities
CREATE CLASS Has extends E
## Account manage many Artists
CREATE CLASS Manage extends E

CREATE PROPERTY Manage.in         LINK
CREATE PROPERTY Manage.out        LINK User
CREATE PROPERTY Manage.territory  STRING
CREATE PROPERTY Manage.type       STRING
CREATE PROPERTY Manage.created_on DATETIME
CREATE PROPERTY Manage.text       STRING
# true for approved, false for pending, delete manage edge for rejected
CREATE PROPERTY Manage.status     STRING

ALTER PROPERTY Manage.type       MANDATORY true
ALTER PROPERTY Manage.created_on DEFAULT sysdate() readonly
ALTER PROPERTY Manage.type       REGEXP  agent|manager|booker|owner
ALTER PROPERTY Manage.status     REGEXP  pending|pending and approved|approved

CREATE INDEX SM_UniqueManages ON Manage(in, out) UNIQUE_HASH_INDEX

ALTER CLASS Manage STRICTMODE true
## Artist based in many locations
## CREATE CLASS Based extends E
## Artist performed at many shows
CREATE CLASS PerformedAt extends E

CREATE PROPERTY PerformedAt.in         LINK
CREATE PROPERTY PerformedAt.out        LINK

CREATE INDEX SM_UniquePerformedAt ON PerformedAt(in, out) UNIQUE_HASH_INDEX

ALTER CLASS PerformedAt STRICTMODE true
## Show is organized by a single/more promoter
CREATE CLASS Organized extends E
## a single profile can follow multiple artist profile, etc...
CREATE CLASS Follow extends E

CREATE PROPERTY Follow.in         LINK
CREATE PROPERTY Follow.out        LINK User
CREATE PROPERTY Follow.created_on DATETIME

ALTER PROPERTY Follow.created_on DEFAULT sysdate() readonly

CREATE INDEX SM_UniqueFollower ON Follow(in, out) UNIQUE_HASH_INDEX

ALTER CLASS Follow STRICTMODE true

## An artist can own multiple social metrics account
CREATE CLASS Own extends E

CREATE PROPERTY Own.in  LINK SocialMetric
CREATE PROPERTY Own.out LINK

ALTER CLASS Own STRICTMODE true
## a single profile can communicate with another profile
CREATE CLASS Converse extends E

CREATE PROPERTY Converse.out          LINK User
## artist profile
CREATE PROPERTY Converse.in           LINK
## users profiles
CREATE PROPERTY Converse.profile_list LINKSET
CREATE PROPERTY Converse.state        STRING
CREATE PROPERTY Converse.created_on   DATETIME
## Layer conversation id
CREATE PROPERTY Converse.layer_id     STRING

ALTER PROPERTY Converse.created_on DEFAULT sysdate() readonly
ALTER PROPERTY Converse.state      DEFAULT "pending"

ALTER CLASS Converse STRICTMODE true

# A Notification belongs to user profile
# so notification is out and profile is in
CREATE CLASS BelongsTo extends E

CREATE PROPERTY BelongsTo.seen    BOOLEAN
CREATE PROPERTY BelongsTo.in      LINK User
CREATE PROPERTY BelongsTo.out     LINK Notification

ALTER PROPERTY BelongsTo.seen     MANDATORY true
ALTER PROPERTY BelongsTo.seen     DEFAULT false

ALTER CLASS BelongsTo STRICTMODE true

# Edge tracking if the user was rejected recently
CREATE CLASS Reject extends E

CREATE PROPERTY Reject.out           LINK User
CREATE PROPERTY Reject.in            LINK
CREATE PROPERTY Reject.created_on    DATETIME

ALTER CLASS Reject STRICTMODE true

# Creates Edge, to link
CREATE CLASS Creates extends E

CREATE PROPERTY Creates.out           LINK
CREATE PROPERTY Creates.in            LINK
# user creates as, could be empty, if available, acting as certain profile
# eg, user -> creates.as = promoter -> bookingrequest -> book -> artist
# CREATE PROPERTY Creates.with          LINK Promoter

ALTER CLASS Creates STRICTMODE true

# Booking edge, eg. bookingrequest -> booking -> artist, bookingrequest -> booking -> venue
CREATE CLASS For extends E

CREATE PROPERTY For.in  LINK
CREATE PROPERTY For.out LINK

ALTER CLASS For STRICTMODE true

# With edge, case - user creates something with promoter or artist profile
CREATE CLASS With extends E

CREATE PROPERTY With.out LINK
CREATE PROPERTY With.in  LINK

ALTER CLASS With STRICTMODE true

# With edge, case - user creates something with promoter or artist profile
CREATE CLASS Changes extends E

CREATE PROPERTY Changes.out LINK
CREATE PROPERTY Changes.in  LINK
CREATE PROPERTY Changes.state STRING

ALTER CLASS Changes STRICTMODE true

# In edge
CREATE CLASS In extends E

CREATE PROPERTY In.out LINK
CREATE PROPERTY In.in  LINK

ALTER CLASS In STRICTMODE true

# At edge
CREATE CLASS At extends E

CREATE PROPERTY At.out LINK
CREATE PROPERTY At.in  LINK

ALTER CLASS At STRICTMODE true

COMMIT
