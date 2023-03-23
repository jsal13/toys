# Graylog

## Status

**Working.**

## Description

An Toy of Graylog running.  

For examples of what to do, check out [the docs](https://docs.graylog.org/docs/docker).

## Quickstart

1. `docker-compose up`.
2. Go to http://localhost:9000/.
3. Add an input ("TCP") in the UI.
4. In terminal, use `echo 'my message' | nc localhost 5555` to send a message to graylog.
5. Go to the messages section to see your message.

## Credentials

- user: `admin`
- password: `secret`
- GRAYLOG_PASSWORD_SECRET: `Aff21H9TVGzsJuSVhR1wvIxWuorJYCwfV9Z3vM0zDie5mzfIR6H2NRkhEuMPWxP5LVQ2FgRj5EtfHrtvJsqr1uZFQ207n5Rr`
- GRAYLOG_ROOT_PASSWORD_SHA2: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`