import Car from './10-car';

class EVCar extends Car {
  constructor(brand, motor, color, range) {
    super();
    this._brand = brand;
    this._motor = motor;
    this._color = color;
    this._range = range;
  }

  cloneCar() {
    const {
      _brand,
      _motor,
      _color,
      _range,
    } = this;
    const clonedCar = new Car();
    clonedCar._brand = _brand;
    clonedCar._motor = _motor;
    clonedCar._color = _color;
    clonedCar._range = _range;
    return clonedCar;
  }
}

export default EVCar;
