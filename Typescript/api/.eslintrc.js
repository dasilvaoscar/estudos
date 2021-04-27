module.exports = {
  env: {
    browser: true,
    es6: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    'plugin:@typescript-eslint/eslint-recommended',
    'plugin:@typescript-eslint/recommended',    
  ],
  globals: {
    Atomics: 'readonly',
    SharedArrayBuffer: 'readonly'
  },
  parser: '@typescript-eslint/parses',
  parserOptions: {
    "ecmaVersion": 11,
    "sourceType": "module",
    "ecmaFeatures": {
        "jsx": true
    }
  },
  plugins: ['@typescript-eslint'],
  rules: {}
}