script sql
begin
update genre set value = "alternative" upsert return after @this where value = "alternative"
update genre set value = "blues" upsert return after @this where value = "blues"
update genre set value = "classical" upsert return after @this where value = "classical"
update genre set value = "comedy" upsert return after @this where value = "comedy"
update genre set value = "country" upsert return after @this where value = "country"
update genre set value = "dance" upsert return after @this where value = "dance"
update genre set value = "electronic" upsert return after @this where value = "electronic"
update genre set value = "pop" upsert return after @this where value = "pop"
update genre set value = "hip-hop" upsert return after @this where value = "hip-hop"
update genre set value = "indie" upsert return after @this where value = "indie"
update genre set value = "international" upsert return after @this where value = "international"
update genre set value = "religious" upsert return after @this where value = "religious"
update genre set value = "instrumental" upsert return after @this where value = "instrumental"
update genre set value = "jazz" upsert return after @this where value = "jazz"
update genre set value = "latin" upsert return after @this where value = "latin"
update genre set value = "new age" upsert return after @this where value = "new age"
update genre set value = "opera" upsert return after @this where value = "opera"
update genre set value = "R&B" upsert return after @this where value = "R&B"
update genre set value = "reggae" upsert return after @this where value = "reggae"
update genre set value = "rock" upsert return after @this where value = "rock"
update genre set value = "vocal" upsert return after @this where value = "vocal"
commit

begin
let oldGenres = select from genre where value="electronic"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="nu disco"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="techno"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="trance"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="house"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="deep"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="dubstep"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="progressive house"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="psychedelic"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="acid"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="2step"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="eurodance"
let genres = select from genre where value IN ["dance","electronic"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="hip-hop"
let genres = select from genre where value IN ["dance","hip-hop"]
update user add genres = $genres where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="breakbeat"
let genres = select from genre where value IN ["dance","hip-hop"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="triphop"
let genres = select from genre where value IN ["dance","hip-hop"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="soul"
let genres = select from genre where value IN ["dance","R&B"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="cyberfunk"
let genres = select from genre where value IN ["dance","R&B"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="boogie"
let genres = select from genre where value IN ["dance","R&B"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="masculino"
let genres = select from genre where value IN ["dance","latin"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="ambient"
let genres = select from genre where value IN ["instrumental","new age"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="lounge"
let genres = select from genre where value IN ["instrumental","new age"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="garage"
let genres = select from genre where value IN ["alternative","rock"]
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="disco"
let genres = select from genre where value="dance"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="jungle"
let genres = select from genre where value="dance"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="groove"
let genres = select from genre where value="dance"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="swing"
let genres = select from genre where value="dance"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="metal"
let genres = select from genre where value="rock"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="gospel"
let genres = select from genre where value="religious"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="blues"
let genres = select from genre where value="R&B"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="funk"
let genres = select from genre where value="R&B"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="tribal"
let genres = select from genre where value="international"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="traditional"
let genres = select from genre where value="international"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="melodic"
let genres = select from genre where value="instrumental"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="rap"
let genres = select from genre where value="hip-hop"
update user add genres = $genres remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="experimental"
update user remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="abstract"
update user remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="minimal"
update user remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="oldschool"
update user remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
let oldGenres = select from genre where value="urban"
update user remove genres= $oldGenres[0] where $oldGenres[0] IN genres
commit

begin
delete vertex genre where value NOT IN ["alternative","blues","classical","comedy","country","dance","electronic","pop","hip-hop","indie","international","religious","instrumental","jazz","latin","new age","opera","R&B","reggae","rock","vocal"]
commit
end
