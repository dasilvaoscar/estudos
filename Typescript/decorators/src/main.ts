function OnRequestError(callback: Function) {
  return function (
    _target: any,
    _propertyKey: string,
    descriptor: PropertyDescriptor
  ) {
    const original = descriptor.value;
  
    descriptor.value = function (...args: any) {
      try {
        return original.call(this, ...args);
      } catch (error) {
        return callback()
      }
    };
  }
}

class CustomersRequest {
  @OnRequestError(() => console.log('Meu metodo'))
  get(error?: boolean) {
    if (error) throw new Error("Method not implemented.");
    return [
      { id: 1, name: "John" },
      { id: 2, name: "Doe" },
    ];
  }
}

const customers = new CustomersRequest();
customers.get(true);
