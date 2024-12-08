import { EventEmitter } from 'node:events';

class PaymentEvents {
  constructor(eventHandler = new EventEmitter()) {
    this.eventHandler = eventHandler
  }

  on(event, ...args) {
    return this.eventHandler.on(event, ...args)
  }

  emit(event, data) {
    return this.eventHandler.emit(event, data)
  }
}

const paymentEvents = new PaymentEvents();

paymentEvents.on('pix_payment', (data) => {
  PixPayment.execute(data)
});

paymentEvents.on('credit_payment', (data) => {
  CreditPayment.execute(data)
});

paymentEvents.on('billet_payment', (data) => {
  BilletPayment.execute(data)
});

paymentEvents.emit('credit_payment', { amount: '8000' });