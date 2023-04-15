module.exports = {
    isDumb(name){
        return (name.includes('Baker') || name.includes('Purvis'));
    },

    hasBase(grade) {
        return (grade >= 10);
    }
};