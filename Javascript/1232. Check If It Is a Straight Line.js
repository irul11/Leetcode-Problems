/**
 * @param {number[][]} coordinates
 * @return {boolean}
 */
var checkStraightLine = function(coordinates) {
    if (coordinates.length === 2) {
        return true;
    }
    let dx1 = coordinates[1][0] - coordinates[0][0];
    let dy1 = coordinates[1][1] - coordinates[0][1];
    const m1 = dy1 === 0 ? 2 * 10 ** -4 : Math.atan(dx1/dy1);

    for (let i = 2; i < coordinates.length; i++) {
        let dx2 = coordinates[i][0] - coordinates[i-1][0];
        let dy2 = coordinates[i][1] - coordinates[i-1][1];
        const m2 = dy2 === 0 ? 2 * 10 ** -4 : Math.atan(dx2/dy2);
        if (m1 != m2) {
            return false;
        }
    }
    return true;
};