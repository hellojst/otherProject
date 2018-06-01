var  person = {
    firstName : 'liu',
    lastName : 'yingchun',
    age : 56,
    eye_color : 'blue',
    say : function (name) {
        return person.firstName + name;
    },
    grow : function (step) {
        person.age += step;
    }
}

person.grow(4);
var str = person.say('say something!');
