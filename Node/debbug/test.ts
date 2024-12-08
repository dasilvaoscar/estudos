export class PixPaymentError extends Error {
  public readonly code: string;
  public readonly metadata?: Record<string, any>;

  constructor(message: string, code: string = 'PIX_PAYMENT_ERROR', metadata?: Record<string, any>) {
    super(message);
    this.name = 'PixPaymentError';
    this.code = code;
    this.metadata = metadata;

    if (Error.captureStackTrace) {
      Error.captureStackTrace(this, PixPaymentError);
    }
  }
}