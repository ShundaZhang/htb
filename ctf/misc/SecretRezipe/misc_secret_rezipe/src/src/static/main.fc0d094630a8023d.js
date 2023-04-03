"use strict";
(self.webpackChunksecret_rezipe = self.webpackChunksecret_rezipe || []).push([[179], {
    365: ()=>{
        function X(n) {
            return "function" == typeof n
        }
        function jo(n) {
            const t = n(r=>{
                Error.call(r),
                r.stack = (new Error).stack
            }
            );
            return t.prototype = Object.create(Error.prototype),
            t.prototype.constructor = t,
            t
        }
        const Ho = jo(n=>function(t) {
            n(this),
            this.message = t ? `${t.length} errors occurred during unsubscription:\n${t.map((r,i)=>`${i + 1}) ${r.toString()}`).join("\n  ")}` : "",
            this.name = "UnsubscriptionError",
            this.errors = t
        }
        );
        function Fr(n, e) {
            if (n) {
                const t = n.indexOf(e);
                0 <= t && n.splice(t, 1)
            }
        }
        class It {
            constructor(e) {
                this.initialTeardown = e,
                this.closed = !1,
                this._parentage = null,
                this._finalizers = null
            }
            unsubscribe() {
                let e;
                if (!this.closed) {
                    this.closed = !0;
                    const {_parentage: t} = this;
                    if (t)
                        if (this._parentage = null,
                        Array.isArray(t))
                            for (const o of t)
                                o.remove(this);
                        else
                            t.remove(this);
                    const {initialTeardown: r} = this;
                    if (X(r))
                        try {
                            r()
                        } catch (o) {
                            e = o instanceof Ho ? o.errors : [o]
                        }
                    const {_finalizers: i} = this;
                    if (i) {
                        this._finalizers = null;
                        for (const o of i)
                            try {
                                If(o)
                            } catch (s) {
                                e = null != e ? e : [],
                                s instanceof Ho ? e = [...e, ...s.errors] : e.push(s)
                            }
                    }
                    if (e)
                        throw new Ho(e)
                }
            }
            add(e) {
                var t;
                if (e && e !== this)
                    if (this.closed)
                        If(e);
                    else {
                        if (e instanceof It) {
                            if (e.closed || e._hasParent(this))
                                return;
                            e._addParent(this)
                        }
                        (this._finalizers = null !== (t = this._finalizers) && void 0 !== t ? t : []).push(e)
                    }
            }
            _hasParent(e) {
                const {_parentage: t} = this;
                return t === e || Array.isArray(t) && t.includes(e)
            }
            _addParent(e) {
                const {_parentage: t} = this;
                this._parentage = Array.isArray(t) ? (t.push(e),
                t) : t ? [t, e] : e
            }
            _removeParent(e) {
                const {_parentage: t} = this;
                t === e ? this._parentage = null : Array.isArray(t) && Fr(t, e)
            }
            remove(e) {
                const {_finalizers: t} = this;
                t && Fr(t, e),
                e instanceof It && e._removeParent(this)
            }
        }
        It.EMPTY = (()=>{
            const n = new It;
            return n.closed = !0,
            n
        }
        )();
        const Af = It.EMPTY;
        function Tf(n) {
            return n instanceof It || n && "closed"in n && X(n.remove) && X(n.add) && X(n.unsubscribe)
        }
        function If(n) {
            X(n) ? n() : n.unsubscribe()
        }
        const tr = {
            onUnhandledError: null,
            onStoppedNotification: null,
            Promise: void 0,
            useDeprecatedSynchronousErrorHandling: !1,
            useDeprecatedNextContext: !1
        }
          , Uo = {
            setTimeout(n, e, ...t) {
                const {delegate: r} = Uo;
                return (null == r ? void 0 : r.setTimeout) ? r.setTimeout(n, e, ...t) : setTimeout(n, e, ...t)
            },
            clearTimeout(n) {
                const {delegate: e} = Uo;
                return ((null == e ? void 0 : e.clearTimeout) || clearTimeout)(n)
            },
            delegate: void 0
        };
        function Sf(n) {
            Uo.setTimeout(()=>{
                const {onUnhandledError: e} = tr;
                if (!e)
                    throw n;
                e(n)
            }
            )
        }
        function al() {}
        const eC = ll("C", void 0, void 0);
        function ll(n, e, t) {
            return {
                kind: n,
                value: e,
                error: t
            }
        }
        let nr = null;
        function $o(n) {
            if (tr.useDeprecatedSynchronousErrorHandling) {
                const e = !nr;
                if (e && (nr = {
                    errorThrown: !1,
                    error: null
                }),
                n(),
                e) {
                    const {errorThrown: t, error: r} = nr;
                    if (nr = null,
                    t)
                        throw r
                }
            } else
                n()
        }
        class ul extends It {
            constructor(e) {
                super(),
                this.isStopped = !1,
                e ? (this.destination = e,
                Tf(e) && e.add(this)) : this.destination = aC
            }
            static create(e, t, r) {
                return new Go(e,t,r)
            }
            next(e) {
                this.isStopped ? dl(function nC(n) {
                    return ll("N", n, void 0)
                }(e), this) : this._next(e)
            }
            error(e) {
                this.isStopped ? dl(function tC(n) {
                    return ll("E", void 0, n)
                }(e), this) : (this.isStopped = !0,
                this._error(e))
            }
            complete() {
                this.isStopped ? dl(eC, this) : (this.isStopped = !0,
                this._complete())
            }
            unsubscribe() {
                this.closed || (this.isStopped = !0,
                super.unsubscribe(),
                this.destination = null)
            }
            _next(e) {
                this.destination.next(e)
            }
            _error(e) {
                try {
                    this.destination.error(e)
                } finally {
                    this.unsubscribe()
                }
            }
            _complete() {
                try {
                    this.destination.complete()
                } finally {
                    this.unsubscribe()
                }
            }
        }
        const iC = Function.prototype.bind;
        function cl(n, e) {
            return iC.call(n, e)
        }
        class oC {
            constructor(e) {
                this.partialObserver = e
            }
            next(e) {
                const {partialObserver: t} = this;
                if (t.next)
                    try {
                        t.next(e)
                    } catch (r) {
                        zo(r)
                    }
            }
            error(e) {
                const {partialObserver: t} = this;
                if (t.error)
                    try {
                        t.error(e)
                    } catch (r) {
                        zo(r)
                    }
                else
                    zo(e)
            }
            complete() {
                const {partialObserver: e} = this;
                if (e.complete)
                    try {
                        e.complete()
                    } catch (t) {
                        zo(t)
                    }
            }
        }
        class Go extends ul {
            constructor(e, t, r) {
                let i;
                if (super(),
                X(e) || !e)
                    i = {
                        next: null != e ? e : void 0,
                        error: null != t ? t : void 0,
                        complete: null != r ? r : void 0
                    };
                else {
                    let o;
                    this && tr.useDeprecatedNextContext ? (o = Object.create(e),
                    o.unsubscribe = ()=>this.unsubscribe(),
                    i = {
                        next: e.next && cl(e.next, o),
                        error: e.error && cl(e.error, o),
                        complete: e.complete && cl(e.complete, o)
                    }) : i = e
                }
                this.destination = new oC(i)
            }
        }
        function zo(n) {
            tr.useDeprecatedSynchronousErrorHandling ? function rC(n) {
                tr.useDeprecatedSynchronousErrorHandling && nr && (nr.errorThrown = !0,
                nr.error = n)
            }(n) : Sf(n)
        }
        function dl(n, e) {
            const {onStoppedNotification: t} = tr;
            t && Uo.setTimeout(()=>t(n, e))
        }
        const aC = {
            closed: !0,
            next: al,
            error: function sC(n) {
                throw n
            },
            complete: al
        }
          , fl = "function" == typeof Symbol && Symbol.observable || "@@observable";
        function qo(n) {
            return n
        }
        let Fe = (()=>{
            class n {
                constructor(t) {
                    t && (this._subscribe = t)
                }
                lift(t) {
                    const r = new n;
                    return r.source = this,
                    r.operator = t,
                    r
                }
                subscribe(t, r, i) {
                    const o = function uC(n) {
                        return n && n instanceof ul || function lC(n) {
                            return n && X(n.next) && X(n.error) && X(n.complete)
                        }(n) && Tf(n)
                    }(t) ? t : new Go(t,r,i);
                    return $o(()=>{
                        const {operator: s, source: a} = this;
                        o.add(s ? s.call(o, a) : a ? this._subscribe(o) : this._trySubscribe(o))
                    }
                    ),
                    o
                }
                _trySubscribe(t) {
                    try {
                        return this._subscribe(t)
                    } catch (r) {
                        t.error(r)
                    }
                }
                forEach(t, r) {
                    return new (r = Ff(r))((i,o)=>{
                        const s = new Go({
                            next: a=>{
                                try {
                                    t(a)
                                } catch (l) {
                                    o(l),
                                    s.unsubscribe()
                                }
                            }
                            ,
                            error: o,
                            complete: i
                        });
                        this.subscribe(s)
                    }
                    )
                }
                _subscribe(t) {
                    var r;
                    return null === (r = this.source) || void 0 === r ? void 0 : r.subscribe(t)
                }
                [fl]() {
                    return this
                }
                pipe(...t) {
                    return function xf(n) {
                        return 0 === n.length ? qo : 1 === n.length ? n[0] : function(t) {
                            return n.reduce((r,i)=>i(r), t)
                        }
                    }(t)(this)
                }
                toPromise(t) {
                    return new (t = Ff(t))((r,i)=>{
                        let o;
                        this.subscribe(s=>o = s, s=>i(s), ()=>r(o))
                    }
                    )
                }
            }
            return n.create = e=>new n(e),
            n
        }
        )();
        function Ff(n) {
            var e;
            return null !== (e = null != n ? n : tr.Promise) && void 0 !== e ? e : Promise
        }
        const cC = jo(n=>function() {
            n(this),
            this.name = "ObjectUnsubscribedError",
            this.message = "object unsubscribed"
        }
        );
        let Ut = (()=>{
            class n extends Fe {
                constructor() {
                    super(),
                    this.closed = !1,
                    this.currentObservers = null,
                    this.observers = [],
                    this.isStopped = !1,
                    this.hasError = !1,
                    this.thrownError = null
                }
                lift(t) {
                    const r = new Nf(this,this);
                    return r.operator = t,
                    r
                }
                _throwIfClosed() {
                    if (this.closed)
                        throw new cC
                }
                next(t) {
                    $o(()=>{
                        if (this._throwIfClosed(),
                        !this.isStopped) {
                            this.currentObservers || (this.currentObservers = Array.from(this.observers));
                            for (const r of this.currentObservers)
                                r.next(t)
                        }
                    }
                    )
                }
                error(t) {
                    $o(()=>{
                        if (this._throwIfClosed(),
                        !this.isStopped) {
                            this.hasError = this.isStopped = !0,
                            this.thrownError = t;
                            const {observers: r} = this;
                            for (; r.length; )
                                r.shift().error(t)
                        }
                    }
                    )
                }
                complete() {
                    $o(()=>{
                        if (this._throwIfClosed(),
                        !this.isStopped) {
                            this.isStopped = !0;
                            const {observers: t} = this;
                            for (; t.length; )
                                t.shift().complete()
                        }
                    }
                    )
                }
                unsubscribe() {
                    this.isStopped = this.closed = !0,
                    this.observers = this.currentObservers = null
                }
                get observed() {
                    var t;
                    return (null === (t = this.observers) || void 0 === t ? void 0 : t.length) > 0
                }
                _trySubscribe(t) {
                    return this._throwIfClosed(),
                    super._trySubscribe(t)
                }
                _subscribe(t) {
                    return this._throwIfClosed(),
                    this._checkFinalizedStatuses(t),
                    this._innerSubscribe(t)
                }
                _innerSubscribe(t) {
                    const {hasError: r, isStopped: i, observers: o} = this;
                    return r || i ? Af : (this.currentObservers = null,
                    o.push(t),
                    new It(()=>{
                        this.currentObservers = null,
                        Fr(o, t)
                    }
                    ))
                }
                _checkFinalizedStatuses(t) {
                    const {hasError: r, thrownError: i, isStopped: o} = this;
                    r ? t.error(i) : o && t.complete()
                }
                asObservable() {
                    const t = new Fe;
                    return t.source = this,
                    t
                }
            }
            return n.create = (e,t)=>new Nf(e,t),
            n
        }
        )();
        class Nf extends Ut {
            constructor(e, t) {
                super(),
                this.destination = e,
                this.source = t
            }
            next(e) {
                var t, r;
                null === (r = null === (t = this.destination) || void 0 === t ? void 0 : t.next) || void 0 === r || r.call(t, e)
            }
            error(e) {
                var t, r;
                null === (r = null === (t = this.destination) || void 0 === t ? void 0 : t.error) || void 0 === r || r.call(t, e)
            }
            complete() {
                var e, t;
                null === (t = null === (e = this.destination) || void 0 === e ? void 0 : e.complete) || void 0 === t || t.call(e)
            }
            _subscribe(e) {
                var t, r;
                return null !== (r = null === (t = this.source) || void 0 === t ? void 0 : t.subscribe(e)) && void 0 !== r ? r : Af
            }
        }
        function st(n) {
            return e=>{
                if (function dC(n) {
                    return X(null == n ? void 0 : n.lift)
                }(e))
                    return e.lift(function(t) {
                        try {
                            return n(t, this)
                        } catch (r) {
                            this.error(r)
                        }
                    });
                throw new TypeError("Unable to lift unknown Observable type")
            }
        }
        function St(n, e, t, r, i) {
            return new fC(n,e,t,r,i)
        }
        class fC extends ul {
            constructor(e, t, r, i, o, s) {
                super(e),
                this.onFinalize = o,
                this.shouldUnsubscribe = s,
                this._next = t ? function(a) {
                    try {
                        t(a)
                    } catch (l) {
                        e.error(l)
                    }
                }
                : super._next,
                this._error = i ? function(a) {
                    try {
                        i(a)
                    } catch (l) {
                        e.error(l)
                    } finally {
                        this.unsubscribe()
                    }
                }
                : super._error,
                this._complete = r ? function() {
                    try {
                        r()
                    } catch (a) {
                        e.error(a)
                    } finally {
                        this.unsubscribe()
                    }
                }
                : super._complete
            }
            unsubscribe() {
                var e;
                if (!this.shouldUnsubscribe || this.shouldUnsubscribe()) {
                    const {closed: t} = this;
                    super.unsubscribe(),
                    !t && (null === (e = this.onFinalize) || void 0 === e || e.call(this))
                }
            }
        }
        function xt(n, e) {
            return st((t,r)=>{
                let i = 0;
                t.subscribe(St(r, o=>{
                    r.next(n.call(e, o, i++))
                }
                ))
            }
            )
        }
        function rr(n) {
            return this instanceof rr ? (this.v = n,
            this) : new rr(n)
        }
        function mC(n, e, t) {
            if (!Symbol.asyncIterator)
                throw new TypeError("Symbol.asyncIterator is not defined.");
            var i, r = t.apply(n, e || []), o = [];
            return i = {},
            s("next"),
            s("throw"),
            s("return"),
            i[Symbol.asyncIterator] = function() {
                return this
            }
            ,
            i;
            function s(f) {
                r[f] && (i[f] = function(h) {
                    return new Promise(function(p, m) {
                        o.push([f, h, p, m]) > 1 || a(f, h)
                    }
                    )
                }
                )
            }
            function a(f, h) {
                try {
                    !function l(f) {
                        f.value instanceof rr ? Promise.resolve(f.value.v).then(u, c) : d(o[0][2], f)
                    }(r[f](h))
                } catch (p) {
                    d(o[0][3], p)
                }
            }
            function u(f) {
                a("next", f)
            }
            function c(f) {
                a("throw", f)
            }
            function d(f, h) {
                f(h),
                o.shift(),
                o.length && a(o[0][0], o[0][1])
            }
        }
        function gC(n) {
            if (!Symbol.asyncIterator)
                throw new TypeError("Symbol.asyncIterator is not defined.");
            var t, e = n[Symbol.asyncIterator];
            return e ? e.call(n) : (n = function Rf(n) {
                var e = "function" == typeof Symbol && Symbol.iterator
                  , t = e && n[e]
                  , r = 0;
                if (t)
                    return t.call(n);
                if (n && "number" == typeof n.length)
                    return {
                        next: function() {
                            return n && r >= n.length && (n = void 0),
                            {
                                value: n && n[r++],
                                done: !n
                            }
                        }
                    };
                throw new TypeError(e ? "Object is not iterable." : "Symbol.iterator is not defined.")
            }(n),
            t = {},
            r("next"),
            r("throw"),
            r("return"),
            t[Symbol.asyncIterator] = function() {
                return this
            }
            ,
            t);
            function r(o) {
                t[o] = n[o] && function(s) {
                    return new Promise(function(a, l) {
                        !function i(o, s, a, l) {
                            Promise.resolve(l).then(function(u) {
                                o({
                                    value: u,
                                    done: a
                                })
                            }, s)
                        }(a, l, (s = n[o](s)).done, s.value)
                    }
                    )
                }
            }
        }
        const pl = n=>n && "number" == typeof n.length && "function" != typeof n;
        function Pf(n) {
            return X(null == n ? void 0 : n.then)
        }
        function Lf(n) {
            return X(n[fl])
        }
        function Vf(n) {
            return Symbol.asyncIterator && X(null == n ? void 0 : n[Symbol.asyncIterator])
        }
        function Bf(n) {
            return new TypeError(`You provided ${null !== n && "object" == typeof n ? "an invalid object" : `'${n}'`} where a stream was expected. You can provide an Observable, Promise, ReadableStream, Array, AsyncIterable, or Iterable.`)
        }
        const jf = function _C() {
            return "function" == typeof Symbol && Symbol.iterator ? Symbol.iterator : "@@iterator"
        }();
        function Hf(n) {
            return X(null == n ? void 0 : n[jf])
        }
        function Uf(n) {
            return mC(this, arguments, function*() {
                const t = n.getReader();
                try {
                    for (; ; ) {
                        const {value: r, done: i} = yield rr(t.read());
                        if (i)
                            return yield rr(void 0);
                        yield yield rr(r)
                    }
                } finally {
                    t.releaseLock()
                }
            })
        }
        function $f(n) {
            return X(null == n ? void 0 : n.getReader)
        }
        function rn(n) {
            if (n instanceof Fe)
                return n;
            if (null != n) {
                if (Lf(n))
                    return function vC(n) {
                        return new Fe(e=>{
                            const t = n[fl]();
                            if (X(t.subscribe))
                                return t.subscribe(e);
                            throw new TypeError("Provided object does not correctly implement Symbol.observable")
                        }
                        )
                    }(n);
                if (pl(n))
                    return function bC(n) {
                        return new Fe(e=>{
                            for (let t = 0; t < n.length && !e.closed; t++)
                                e.next(n[t]);
                            e.complete()
                        }
                        )
                    }(n);
                if (Pf(n))
                    return function DC(n) {
                        return new Fe(e=>{
                            n.then(t=>{
                                e.closed || (e.next(t),
                                e.complete())
                            }
                            , t=>e.error(t)).then(null, Sf)
                        }
                        )
                    }(n);
                if (Vf(n))
                    return Gf(n);
                if (Hf(n))
                    return function CC(n) {
                        return new Fe(e=>{
                            for (const t of n)
                                if (e.next(t),
                                e.closed)
                                    return;
                            e.complete()
                        }
                        )
                    }(n);
                if ($f(n))
                    return function EC(n) {
                        return Gf(Uf(n))
                    }(n)
            }
            throw Bf(n)
        }
        function Gf(n) {
            return new Fe(e=>{
                (function wC(n, e) {
                    var t, r, i, o;
                    return function hC(n, e, t, r) {
                        return new (t || (t = Promise))(function(o, s) {
                            function a(c) {
                                try {
                                    u(r.next(c))
                                } catch (d) {
                                    s(d)
                                }
                            }
                            function l(c) {
                                try {
                                    u(r.throw(c))
                                } catch (d) {
                                    s(d)
                                }
                            }
                            function u(c) {
                                c.done ? o(c.value) : function i(o) {
                                    return o instanceof t ? o : new t(function(s) {
                                        s(o)
                                    }
                                    )
                                }(c.value).then(a, l)
                            }
                            u((r = r.apply(n, e || [])).next())
                        }
                        )
                    }(this, void 0, void 0, function*() {
                        try {
                            for (t = gC(n); !(r = yield t.next()).done; )
                                if (e.next(r.value),
                                e.closed)
                                    return
                        } catch (s) {
                            i = {
                                error: s
                            }
                        } finally {
                            try {
                                r && !r.done && (o = t.return) && (yield o.call(t))
                            } finally {
                                if (i)
                                    throw i.error
                            }
                        }
                        e.complete()
                    })
                }
                )(n, e).catch(t=>e.error(t))
            }
            )
        }
        function kn(n, e, t, r=0, i=!1) {
            const o = e.schedule(function() {
                t(),
                i ? n.add(this.schedule(null, r)) : this.unsubscribe()
            }, r);
            if (n.add(o),
            !i)
                return o
        }
        function xi(n, e, t=1 / 0) {
            return X(e) ? xi((r,i)=>xt((o,s)=>e(r, o, i, s))(rn(n(r, i))), t) : ("number" == typeof e && (t = e),
            st((r,i)=>function MC(n, e, t, r, i, o, s, a) {
                const l = [];
                let u = 0
                  , c = 0
                  , d = !1;
                const f = ()=>{
                    d && !l.length && !u && e.complete()
                }
                  , h = m=>u < r ? p(m) : l.push(m)
                  , p = m=>{
                    o && e.next(m),
                    u++;
                    let y = !1;
                    rn(t(m, c++)).subscribe(St(e, _=>{
                        null == i || i(_),
                        o ? h(_) : e.next(_)
                    }
                    , ()=>{
                        y = !0
                    }
                    , void 0, ()=>{
                        if (y)
                            try {
                                for (u--; l.length && u < r; ) {
                                    const _ = l.shift();
                                    s ? kn(e, s, ()=>p(_)) : p(_)
                                }
                                f()
                            } catch (_) {
                                e.error(_)
                            }
                    }
                    ))
                }
                ;
                return n.subscribe(St(e, h, ()=>{
                    d = !0,
                    f()
                }
                )),
                ()=>{
                    null == a || a()
                }
            }(r, i, n, t)))
        }
        function zf(n=1 / 0) {
            return xi(qo, n)
        }
        const Wo = new Fe(n=>n.complete());
        function ml(n) {
            return n[n.length - 1]
        }
        function Ko(n) {
            return function TC(n) {
                return n && X(n.schedule)
            }(ml(n)) ? n.pop() : void 0
        }
        function qf(n, e=0) {
            return st((t,r)=>{
                t.subscribe(St(r, i=>kn(r, n, ()=>r.next(i), e), ()=>kn(r, n, ()=>r.complete(), e), i=>kn(r, n, ()=>r.error(i), e)))
            }
            )
        }
        function Wf(n, e=0) {
            return st((t,r)=>{
                r.add(n.schedule(()=>t.subscribe(r), e))
            }
            )
        }
        function Kf(n, e) {
            if (!n)
                throw new Error("Iterable cannot be null");
            return new Fe(t=>{
                kn(t, e, ()=>{
                    const r = n[Symbol.asyncIterator]();
                    kn(t, e, ()=>{
                        r.next().then(i=>{
                            i.done ? t.complete() : t.next(i.value)
                        }
                        )
                    }
                    , 0, !0)
                }
                )
            }
            )
        }
        function Fi(n, e) {
            return e ? function RC(n, e) {
                if (null != n) {
                    if (Lf(n))
                        return function xC(n, e) {
                            return rn(n).pipe(Wf(e), qf(e))
                        }(n, e);
                    if (pl(n))
                        return function NC(n, e) {
                            return new Fe(t=>{
                                let r = 0;
                                return e.schedule(function() {
                                    r === n.length ? t.complete() : (t.next(n[r++]),
                                    t.closed || this.schedule())
                                })
                            }
                            )
                        }(n, e);
                    if (Pf(n))
                        return function FC(n, e) {
                            return rn(n).pipe(Wf(e), qf(e))
                        }(n, e);
                    if (Vf(n))
                        return Kf(n, e);
                    if (Hf(n))
                        return function OC(n, e) {
                            return new Fe(t=>{
                                let r;
                                return kn(t, e, ()=>{
                                    r = n[jf](),
                                    kn(t, e, ()=>{
                                        let i, o;
                                        try {
                                            ({value: i, done: o} = r.next())
                                        } catch (s) {
                                            return void t.error(s)
                                        }
                                        o ? t.complete() : t.next(i)
                                    }
                                    , 0, !0)
                                }
                                ),
                                ()=>X(null == r ? void 0 : r.return) && r.return()
                            }
                            )
                        }(n, e);
                    if ($f(n))
                        return function kC(n, e) {
                            return Kf(Uf(n), e)
                        }(n, e)
                }
                throw Bf(n)
            }(n, e) : rn(n)
        }
        function Qf(...n) {
            const e = Ko(n)
              , t = function SC(n, e) {
                return "number" == typeof ml(n) ? n.pop() : e
            }(n, 1 / 0)
              , r = n;
            return r.length ? 1 === r.length ? rn(r[0]) : zf(t)(Fi(r, e)) : Wo
        }
        function gl(n) {
            return n <= 0 ? ()=>Wo : st((e,t)=>{
                let r = 0;
                e.subscribe(St(t, i=>{
                    ++r <= n && (t.next(i),
                    n <= r && t.complete())
                }
                ))
            }
            )
        }
        function Zf(n={}) {
            const {connector: e=(()=>new Ut), resetOnError: t=!0, resetOnComplete: r=!0, resetOnRefCountZero: i=!0} = n;
            return o=>{
                let s = null
                  , a = null
                  , l = null
                  , u = 0
                  , c = !1
                  , d = !1;
                const f = ()=>{
                    null == a || a.unsubscribe(),
                    a = null
                }
                  , h = ()=>{
                    f(),
                    s = l = null,
                    c = d = !1
                }
                  , p = ()=>{
                    const m = s;
                    h(),
                    null == m || m.unsubscribe()
                }
                ;
                return st((m,y)=>{
                    u++,
                    !d && !c && f();
                    const _ = l = null != l ? l : e();
                    y.add(()=>{
                        u--,
                        0 === u && !d && !c && (a = yl(p, i))
                    }
                    ),
                    _.subscribe(y),
                    s || (s = new Go({
                        next: g=>_.next(g),
                        error: g=>{
                            d = !0,
                            f(),
                            a = yl(h, t, g),
                            _.error(g)
                        }
                        ,
                        complete: ()=>{
                            c = !0,
                            f(),
                            a = yl(h, r),
                            _.complete()
                        }
                    }),
                    Fi(m).subscribe(s))
                }
                )(o)
            }
        }
        function yl(n, e, ...t) {
            return !0 === e ? (n(),
            null) : !1 === e ? null : e(...t).pipe(gl(1)).subscribe(()=>n())
        }
        function re(n) {
            for (let e in n)
                if (n[e] === re)
                    return e;
            throw Error("Could not find renamed property on target object.")
        }
        function _l(n, e) {
            for (const t in e)
                e.hasOwnProperty(t) && !n.hasOwnProperty(t) && (n[t] = e[t])
        }
        function te(n) {
            if ("string" == typeof n)
                return n;
            if (Array.isArray(n))
                return "[" + n.map(te).join(", ") + "]";
            if (null == n)
                return "" + n;
            if (n.overriddenName)
                return `${n.overriddenName}`;
            if (n.name)
                return `${n.name}`;
            const e = n.toString();
            if (null == e)
                return "" + e;
            const t = e.indexOf("\n");
            return -1 === t ? e : e.substring(0, t)
        }
        function vl(n, e) {
            return null == n || "" === n ? null === e ? "" : e : null == e || "" === e ? n : n + " " + e
        }
        const PC = re({
            __forward_ref__: re
        });
        function oe(n) {
            return n.__forward_ref__ = oe,
            n.toString = function() {
                return te(this())
            }
            ,
            n
        }
        function U(n) {
            return Yf(n) ? n() : n
        }
        function Yf(n) {
            return "function" == typeof n && n.hasOwnProperty(PC) && n.__forward_ref__ === oe
        }
        class M extends Error {
            constructor(e, t) {
                super(function bl(n, e) {
                    return `NG0${Math.abs(n)}${e ? ": " + e : ""}`
                }(e, t)),
                this.code = e
            }
        }
        function L(n) {
            return "string" == typeof n ? n : null == n ? "" : String(n)
        }
        function Ue(n) {
            return "function" == typeof n ? n.name || n.toString() : "object" == typeof n && null != n && "function" == typeof n.type ? n.type.name || n.type.toString() : L(n)
        }
        function Qo(n, e) {
            const t = e ? ` in ${e}` : "";
            throw new M(-201,`No provider for ${Ue(n)} found${t}`)
        }
        function ft(n, e) {
            null == n && function ue(n, e, t, r) {
                throw new Error(`ASSERTION ERROR: ${n}` + (null == r ? "" : ` [Expected=> ${t} ${r} ${e} <=Actual]`))
            }(e, n, null, "!=")
        }
        function R(n) {
            return {
                token: n.token,
                providedIn: n.providedIn || null,
                factory: n.factory,
                value: void 0
            }
        }
        function ce(n) {
            return {
                providers: n.providers || [],
                imports: n.imports || []
            }
        }
        function Dl(n) {
            return Xf(n, Zo) || Xf(n, eh)
        }
        function Xf(n, e) {
            return n.hasOwnProperty(e) ? n[e] : null
        }
        function Jf(n) {
            return n && (n.hasOwnProperty(Cl) || n.hasOwnProperty($C)) ? n[Cl] : null
        }
        const Zo = re({
            \u0275prov: re
        })
          , Cl = re({
            \u0275inj: re
        })
          , eh = re({
            ngInjectableDef: re
        })
          , $C = re({
            ngInjectorDef: re
        });
        var H = (()=>((H = H || {})[H.Default = 0] = "Default",
        H[H.Host = 1] = "Host",
        H[H.Self = 2] = "Self",
        H[H.SkipSelf = 4] = "SkipSelf",
        H[H.Optional = 8] = "Optional",
        H))();
        let El;
        function Rn(n) {
            const e = El;
            return El = n,
            e
        }
        function th(n, e, t) {
            const r = Dl(n);
            return r && "root" == r.providedIn ? void 0 === r.value ? r.value = r.factory() : r.value : t & H.Optional ? null : void 0 !== e ? e : void Qo(te(n), "Injector")
        }
        function Pn(n) {
            return {
                toString: n
            }.toString()
        }
        var $t = (()=>(($t = $t || {})[$t.OnPush = 0] = "OnPush",
        $t[$t.Default = 1] = "Default",
        $t))()
          , Gt = (()=>{
            return (n = Gt || (Gt = {}))[n.Emulated = 0] = "Emulated",
            n[n.None = 2] = "None",
            n[n.ShadowDom = 3] = "ShadowDom",
            Gt;
            var n
        }
        )();
        const zC = "undefined" != typeof globalThis && globalThis
          , qC = "undefined" != typeof window && window
          , WC = "undefined" != typeof self && "undefined" != typeof WorkerGlobalScope && self instanceof WorkerGlobalScope && self
          , ne = zC || "undefined" != typeof global && global || qC || WC
          , Nr = {}
          , ie = []
          , Yo = re({
            \u0275cmp: re
        })
          , wl = re({
            \u0275dir: re
        })
          , Ml = re({
            \u0275pipe: re
        })
          , nh = re({
            \u0275mod: re
        })
          , Cn = re({
            \u0275fac: re
        })
          , Ni = re({
            __NG_ELEMENT_ID__: re
        });
        let KC = 0;
        function Ft(n) {
            return Pn(()=>{
                const t = {}
                  , r = {
                    type: n.type,
                    providersResolver: null,
                    decls: n.decls,
                    vars: n.vars,
                    factory: null,
                    template: n.template || null,
                    consts: n.consts || null,
                    ngContentSelectors: n.ngContentSelectors,
                    hostBindings: n.hostBindings || null,
                    hostVars: n.hostVars || 0,
                    hostAttrs: n.hostAttrs || null,
                    contentQueries: n.contentQueries || null,
                    declaredInputs: t,
                    inputs: null,
                    outputs: null,
                    exportAs: n.exportAs || null,
                    onPush: n.changeDetection === $t.OnPush,
                    directiveDefs: null,
                    pipeDefs: null,
                    selectors: n.selectors || ie,
                    viewQuery: n.viewQuery || null,
                    features: n.features || null,
                    data: n.data || {},
                    encapsulation: n.encapsulation || Gt.Emulated,
                    id: "c",
                    styles: n.styles || ie,
                    _: null,
                    setInput: null,
                    schemas: n.schemas || null,
                    tView: null
                }
                  , i = n.directives
                  , o = n.features
                  , s = n.pipes;
                return r.id += KC++,
                r.inputs = sh(n.inputs, t),
                r.outputs = sh(n.outputs),
                o && o.forEach(a=>a(r)),
                r.directiveDefs = i ? ()=>("function" == typeof i ? i() : i).map(rh) : null,
                r.pipeDefs = s ? ()=>("function" == typeof s ? s() : s).map(ih) : null,
                r
            }
            )
        }
        function rh(n) {
            return $e(n) || function Ln(n) {
                return n[wl] || null
            }(n)
        }
        function ih(n) {
            return function ir(n) {
                return n[Ml] || null
            }(n)
        }
        const oh = {};
        function he(n) {
            return Pn(()=>{
                const e = {
                    type: n.type,
                    bootstrap: n.bootstrap || ie,
                    declarations: n.declarations || ie,
                    imports: n.imports || ie,
                    exports: n.exports || ie,
                    transitiveCompileScopes: null,
                    schemas: n.schemas || null,
                    id: n.id || null
                };
                return null != n.id && (oh[n.id] = n.type),
                e
            }
            )
        }
        function sh(n, e) {
            if (null == n)
                return Nr;
            const t = {};
            for (const r in n)
                if (n.hasOwnProperty(r)) {
                    let i = n[r]
                      , o = i;
                    Array.isArray(i) && (o = i[1],
                    i = i[0]),
                    t[i] = r,
                    e && (e[i] = o)
                }
            return t
        }
        const x = Ft;
        function $e(n) {
            return n[Yo] || null
        }
        function Nt(n, e) {
            const t = n[nh] || null;
            if (!t && !0 === e)
                throw new Error(`Type ${te(n)} does not have '\u0275mod' property.`);
            return t
        }
        const $ = 11;
        function on(n) {
            return Array.isArray(n) && "object" == typeof n[1]
        }
        function qt(n) {
            return Array.isArray(n) && !0 === n[1]
        }
        function Il(n) {
            return 0 != (8 & n.flags)
        }
        function ts(n) {
            return 2 == (2 & n.flags)
        }
        function ns(n) {
            return 1 == (1 & n.flags)
        }
        function Wt(n) {
            return null !== n.template
        }
        function eE(n) {
            return 0 != (512 & n[2])
        }
        function lr(n, e) {
            return n.hasOwnProperty(Cn) ? n[Cn] : null
        }
        class rE {
            constructor(e, t, r) {
                this.previousValue = e,
                this.currentValue = t,
                this.firstChange = r
            }
            isFirstChange() {
                return this.firstChange
            }
        }
        function sn() {
            return lh
        }
        function lh(n) {
            return n.type.prototype.ngOnChanges && (n.setInput = oE),
            iE
        }
        function iE() {
            const n = ch(this)
              , e = null == n ? void 0 : n.current;
            if (e) {
                const t = n.previous;
                if (t === Nr)
                    n.previous = e;
                else
                    for (let r in e)
                        t[r] = e[r];
                n.current = null,
                this.ngOnChanges(e)
            }
        }
        function oE(n, e, t, r) {
            const i = ch(n) || function sE(n, e) {
                return n[uh] = e
            }(n, {
                previous: Nr,
                current: null
            })
              , o = i.current || (i.current = {})
              , s = i.previous
              , a = this.declaredInputs[t]
              , l = s[a];
            o[a] = new rE(l && l.currentValue,e,s === Nr),
            n[r] = e
        }
        sn.ngInherit = !0;
        const uh = "__ngSimpleChanges__";
        function ch(n) {
            return n[uh] || null
        }
        let Ol;
        function Ce(n) {
            return !!n.listen
        }
        const dh = {
            createRenderer: (n,e)=>function kl() {
                return void 0 !== Ol ? Ol : "undefined" != typeof document ? document : void 0
            }()
        };
        function Te(n) {
            for (; Array.isArray(n); )
                n = n[0];
            return n
        }
        function rs(n, e) {
            return Te(e[n])
        }
        function Rt(n, e) {
            return Te(e[n.index])
        }
        function Rl(n, e) {
            return n.data[e]
        }
        function pt(n, e) {
            const t = e[n];
            return on(t) ? t : t[0]
        }
        function fh(n) {
            return 4 == (4 & n[2])
        }
        function Pl(n) {
            return 128 == (128 & n[2])
        }
        function Vn(n, e) {
            return null == e ? null : n[e]
        }
        function hh(n) {
            n[18] = 0
        }
        function Ll(n, e) {
            n[5] += e;
            let t = n
              , r = n[3];
            for (; null !== r && (1 === e && 1 === t[5] || -1 === e && 0 === t[5]); )
                r[5] += e,
                t = r,
                r = r[3]
        }
        const P = {
            lFrame: Dh(null),
            bindingsEnabled: !0,
            isInCheckNoChangesMode: !1
        };
        function ph() {
            return P.bindingsEnabled
        }
        function b() {
            return P.lFrame.lView
        }
        function Q() {
            return P.lFrame.tView
        }
        function Vl(n) {
            return P.lFrame.contextLView = n,
            n[8]
        }
        function Ne() {
            let n = mh();
            for (; null !== n && 64 === n.type; )
                n = n.parent;
            return n
        }
        function mh() {
            return P.lFrame.currentTNode
        }
        function an(n, e) {
            const t = P.lFrame;
            t.currentTNode = n,
            t.isParent = e
        }
        function Bl() {
            return P.lFrame.isParent
        }
        function jl() {
            P.lFrame.isParent = !1
        }
        function is() {
            return P.isInCheckNoChangesMode
        }
        function os(n) {
            P.isInCheckNoChangesMode = n
        }
        function Vr() {
            return P.lFrame.bindingIndex++
        }
        function EE(n, e) {
            const t = P.lFrame;
            t.bindingIndex = t.bindingRootIndex = n,
            Hl(e)
        }
        function Hl(n) {
            P.lFrame.currentDirectiveIndex = n
        }
        function _h() {
            return P.lFrame.currentQueryIndex
        }
        function $l(n) {
            P.lFrame.currentQueryIndex = n
        }
        function ME(n) {
            const e = n[1];
            return 2 === e.type ? e.declTNode : 1 === e.type ? n[6] : null
        }
        function vh(n, e, t) {
            if (t & H.SkipSelf) {
                let i = e
                  , o = n;
                for (; !(i = i.parent,
                null !== i || t & H.Host || (i = ME(o),
                null === i || (o = o[15],
                10 & i.type))); )
                    ;
                if (null === i)
                    return !1;
                e = i,
                n = o
            }
            const r = P.lFrame = bh();
            return r.currentTNode = e,
            r.lView = n,
            !0
        }
        function ss(n) {
            const e = bh()
              , t = n[1];
            P.lFrame = e,
            e.currentTNode = t.firstChild,
            e.lView = n,
            e.tView = t,
            e.contextLView = n,
            e.bindingIndex = t.bindingStartIndex,
            e.inI18n = !1
        }
        function bh() {
            const n = P.lFrame
              , e = null === n ? null : n.child;
            return null === e ? Dh(n) : e
        }
        function Dh(n) {
            const e = {
                currentTNode: null,
                isParent: !0,
                lView: null,
                tView: null,
                selectedIndex: -1,
                contextLView: null,
                elementDepthCount: 0,
                currentNamespace: null,
                currentDirectiveIndex: -1,
                bindingRootIndex: -1,
                bindingIndex: -1,
                currentQueryIndex: 0,
                parent: n,
                child: null,
                inI18n: !1
            };
            return null !== n && (n.child = e),
            e
        }
        function Ch() {
            const n = P.lFrame;
            return P.lFrame = n.parent,
            n.currentTNode = null,
            n.lView = null,
            n
        }
        const Eh = Ch;
        function as() {
            const n = Ch();
            n.isParent = !0,
            n.tView = null,
            n.selectedIndex = -1,
            n.contextLView = null,
            n.elementDepthCount = 0,
            n.currentDirectiveIndex = -1,
            n.currentNamespace = null,
            n.bindingRootIndex = -1,
            n.bindingIndex = -1,
            n.currentQueryIndex = 0
        }
        function Ye() {
            return P.lFrame.selectedIndex
        }
        function Bn(n) {
            P.lFrame.selectedIndex = n
        }
        function Ee() {
            const n = P.lFrame;
            return Rl(n.tView, n.selectedIndex)
        }
        function ls(n, e) {
            for (let t = e.directiveStart, r = e.directiveEnd; t < r; t++) {
                const o = n.data[t].type.prototype
                  , {ngAfterContentInit: s, ngAfterContentChecked: a, ngAfterViewInit: l, ngAfterViewChecked: u, ngOnDestroy: c} = o;
                s && (n.contentHooks || (n.contentHooks = [])).push(-t, s),
                a && ((n.contentHooks || (n.contentHooks = [])).push(t, a),
                (n.contentCheckHooks || (n.contentCheckHooks = [])).push(t, a)),
                l && (n.viewHooks || (n.viewHooks = [])).push(-t, l),
                u && ((n.viewHooks || (n.viewHooks = [])).push(t, u),
                (n.viewCheckHooks || (n.viewCheckHooks = [])).push(t, u)),
                null != c && (n.destroyHooks || (n.destroyHooks = [])).push(t, c)
            }
        }
        function us(n, e, t) {
            wh(n, e, 3, t)
        }
        function cs(n, e, t, r) {
            (3 & n[2]) === t && wh(n, e, t, r)
        }
        function Gl(n, e) {
            let t = n[2];
            (3 & t) === e && (t &= 2047,
            t += 1,
            n[2] = t)
        }
        function wh(n, e, t, r) {
            const o = null != r ? r : -1
              , s = e.length - 1;
            let a = 0;
            for (let l = void 0 !== r ? 65535 & n[18] : 0; l < s; l++)
                if ("number" == typeof e[l + 1]) {
                    if (a = e[l],
                    null != r && a >= r)
                        break
                } else
                    e[l] < 0 && (n[18] += 65536),
                    (a < o || -1 == o) && (kE(n, t, e, l),
                    n[18] = (4294901760 & n[18]) + l + 2),
                    l++
        }
        function kE(n, e, t, r) {
            const i = t[r] < 0
              , o = t[r + 1]
              , a = n[i ? -t[r] : t[r]];
            if (i) {
                if (n[2] >> 11 < n[18] >> 16 && (3 & n[2]) === e) {
                    n[2] += 2048;
                    try {
                        o.call(a)
                    } finally {}
                }
            } else
                try {
                    o.call(a)
                } finally {}
        }
        class Li {
            constructor(e, t, r) {
                this.factory = e,
                this.resolving = !1,
                this.canSeeViewProviders = t,
                this.injectImpl = r
            }
        }
        function ds(n, e, t) {
            const r = Ce(n);
            let i = 0;
            for (; i < t.length; ) {
                const o = t[i];
                if ("number" == typeof o) {
                    if (0 !== o)
                        break;
                    i++;
                    const s = t[i++]
                      , a = t[i++]
                      , l = t[i++];
                    r ? n.setAttribute(e, a, l, s) : e.setAttributeNS(s, a, l)
                } else {
                    const s = o
                      , a = t[++i];
                    ql(s) ? r && n.setProperty(e, s, a) : r ? n.setAttribute(e, s, a) : e.setAttribute(s, a),
                    i++
                }
            }
            return i
        }
        function Mh(n) {
            return 3 === n || 4 === n || 6 === n
        }
        function ql(n) {
            return 64 === n.charCodeAt(0)
        }
        function fs(n, e) {
            if (null !== e && 0 !== e.length)
                if (null === n || 0 === n.length)
                    n = e.slice();
                else {
                    let t = -1;
                    for (let r = 0; r < e.length; r++) {
                        const i = e[r];
                        "number" == typeof i ? t = i : 0 === t || Ah(n, t, i, null, -1 === t || 2 === t ? e[++r] : null)
                    }
                }
            return n
        }
        function Ah(n, e, t, r, i) {
            let o = 0
              , s = n.length;
            if (-1 === e)
                s = -1;
            else
                for (; o < n.length; ) {
                    const a = n[o++];
                    if ("number" == typeof a) {
                        if (a === e) {
                            s = -1;
                            break
                        }
                        if (a > e) {
                            s = o - 1;
                            break
                        }
                    }
                }
            for (; o < n.length; ) {
                const a = n[o];
                if ("number" == typeof a)
                    break;
                if (a === t) {
                    if (null === r)
                        return void (null !== i && (n[o + 1] = i));
                    if (r === n[o + 1])
                        return void (n[o + 2] = i)
                }
                o++,
                null !== r && o++,
                null !== i && o++
            }
            -1 !== s && (n.splice(s, 0, e),
            o = s + 1),
            n.splice(o++, 0, t),
            null !== r && n.splice(o++, 0, r),
            null !== i && n.splice(o++, 0, i)
        }
        function Th(n) {
            return -1 !== n
        }
        function Br(n) {
            return 32767 & n
        }
        function jr(n, e) {
            let t = function BE(n) {
                return n >> 16
            }(n)
              , r = e;
            for (; t > 0; )
                r = r[15],
                t--;
            return r
        }
        let Wl = !0;
        function hs(n) {
            const e = Wl;
            return Wl = n,
            e
        }
        let jE = 0;
        function Bi(n, e) {
            const t = Ql(n, e);
            if (-1 !== t)
                return t;
            const r = e[1];
            r.firstCreatePass && (n.injectorIndex = e.length,
            Kl(r.data, n),
            Kl(e, null),
            Kl(r.blueprint, null));
            const i = ps(n, e)
              , o = n.injectorIndex;
            if (Th(i)) {
                const s = Br(i)
                  , a = jr(i, e)
                  , l = a[1].data;
                for (let u = 0; u < 8; u++)
                    e[o + u] = a[s + u] | l[s + u]
            }
            return e[o + 8] = i,
            o
        }
        function Kl(n, e) {
            n.push(0, 0, 0, 0, 0, 0, 0, 0, e)
        }
        function Ql(n, e) {
            return -1 === n.injectorIndex || n.parent && n.parent.injectorIndex === n.injectorIndex || null === e[n.injectorIndex + 8] ? -1 : n.injectorIndex
        }
        function ps(n, e) {
            if (n.parent && -1 !== n.parent.injectorIndex)
                return n.parent.injectorIndex;
            let t = 0
              , r = null
              , i = e;
            for (; null !== i; ) {
                const o = i[1]
                  , s = o.type;
                if (r = 2 === s ? o.declTNode : 1 === s ? i[6] : null,
                null === r)
                    return -1;
                if (t++,
                i = i[15],
                -1 !== r.injectorIndex)
                    return r.injectorIndex | t << 16
            }
            return -1
        }
        function ms(n, e, t) {
            !function HE(n, e, t) {
                let r;
                "string" == typeof t ? r = t.charCodeAt(0) || 0 : t.hasOwnProperty(Ni) && (r = t[Ni]),
                null == r && (r = t[Ni] = jE++);
                const i = 255 & r;
                e.data[n + (i >> 5)] |= 1 << i
            }(n, e, t)
        }
        function xh(n, e, t) {
            if (t & H.Optional)
                return n;
            Qo(e, "NodeInjector")
        }
        function Fh(n, e, t, r) {
            if (t & H.Optional && void 0 === r && (r = null),
            0 == (t & (H.Self | H.Host))) {
                const i = n[9]
                  , o = Rn(void 0);
                try {
                    return i ? i.get(e, r, t & H.Optional) : th(e, r, t & H.Optional)
                } finally {
                    Rn(o)
                }
            }
            return xh(r, e, t)
        }
        function Nh(n, e, t, r=H.Default, i) {
            if (null !== n) {
                const o = function zE(n) {
                    if ("string" == typeof n)
                        return n.charCodeAt(0) || 0;
                    const e = n.hasOwnProperty(Ni) ? n[Ni] : void 0;
                    return "number" == typeof e ? e >= 0 ? 255 & e : $E : e
                }(t);
                if ("function" == typeof o) {
                    if (!vh(e, n, r))
                        return r & H.Host ? xh(i, t, r) : Fh(e, t, r, i);
                    try {
                        const s = o(r);
                        if (null != s || r & H.Optional)
                            return s;
                        Qo(t)
                    } finally {
                        Eh()
                    }
                } else if ("number" == typeof o) {
                    let s = null
                      , a = Ql(n, e)
                      , l = -1
                      , u = r & H.Host ? e[16][6] : null;
                    for ((-1 === a || r & H.SkipSelf) && (l = -1 === a ? ps(n, e) : e[a + 8],
                    -1 !== l && Rh(r, !1) ? (s = e[1],
                    a = Br(l),
                    e = jr(l, e)) : a = -1); -1 !== a; ) {
                        const c = e[1];
                        if (kh(o, a, c.data)) {
                            const d = GE(a, e, t, s, r, u);
                            if (d !== Oh)
                                return d
                        }
                        l = e[a + 8],
                        -1 !== l && Rh(r, e[1].data[a + 8] === u) && kh(o, a, e) ? (s = c,
                        a = Br(l),
                        e = jr(l, e)) : a = -1
                    }
                }
            }
            return Fh(e, t, r, i)
        }
        const Oh = {};
        function $E() {
            return new Hr(Ne(),b())
        }
        function GE(n, e, t, r, i, o) {
            const s = e[1]
              , a = s.data[n + 8]
              , c = gs(a, s, t, null == r ? ts(a) && Wl : r != s && 0 != (3 & a.type), i & H.Host && o === a);
            return null !== c ? ji(e, s, c, a) : Oh
        }
        function gs(n, e, t, r, i) {
            const o = n.providerIndexes
              , s = e.data
              , a = 1048575 & o
              , l = n.directiveStart
              , c = o >> 20
              , f = i ? a + c : n.directiveEnd;
            for (let h = r ? a : a + c; h < f; h++) {
                const p = s[h];
                if (h < l && t === p || h >= l && p.type === t)
                    return h
            }
            if (i) {
                const h = s[l];
                if (h && Wt(h) && h.type === t)
                    return l
            }
            return null
        }
        function ji(n, e, t, r) {
            let i = n[t];
            const o = e.data;
            if (function RE(n) {
                return n instanceof Li
            }(i)) {
                const s = i;
                s.resolving && function LC(n, e) {
                    const t = e ? `. Dependency path: ${e.join(" > ")} > ${n}` : "";
                    throw new M(-200,`Circular dependency in DI detected for ${n}${t}`)
                }(Ue(o[t]));
                const a = hs(s.canSeeViewProviders);
                s.resolving = !0;
                const l = s.injectImpl ? Rn(s.injectImpl) : null;
                vh(n, r, H.Default);
                try {
                    i = n[t] = s.factory(void 0, o, n, r),
                    e.firstCreatePass && t >= r.directiveStart && function OE(n, e, t) {
                        const {ngOnChanges: r, ngOnInit: i, ngDoCheck: o} = e.type.prototype;
                        if (r) {
                            const s = lh(e);
                            (t.preOrderHooks || (t.preOrderHooks = [])).push(n, s),
                            (t.preOrderCheckHooks || (t.preOrderCheckHooks = [])).push(n, s)
                        }
                        i && (t.preOrderHooks || (t.preOrderHooks = [])).push(0 - n, i),
                        o && ((t.preOrderHooks || (t.preOrderHooks = [])).push(n, o),
                        (t.preOrderCheckHooks || (t.preOrderCheckHooks = [])).push(n, o))
                    }(t, o[t], e)
                } finally {
                    null !== l && Rn(l),
                    hs(a),
                    s.resolving = !1,
                    Eh()
                }
            }
            return i
        }
        function kh(n, e, t) {
            return !!(t[e + (n >> 5)] & 1 << n)
        }
        function Rh(n, e) {
            return !(n & H.Self || n & H.Host && e)
        }
        class Hr {
            constructor(e, t) {
                this._tNode = e,
                this._lView = t
            }
            get(e, t, r) {
                return Nh(this._tNode, this._lView, e, r, t)
            }
        }
        function Zl(n) {
            return Yf(n) ? ()=>{
                const e = Zl(U(n));
                return e && e()
            }
            : lr(n)
        }
        const $r = "__parameters__";
        function zr(n, e, t) {
            return Pn(()=>{
                const r = function Yl(n) {
                    return function(...t) {
                        if (n) {
                            const r = n(...t);
                            for (const i in r)
                                this[i] = r[i]
                        }
                    }
                }(e);
                function i(...o) {
                    if (this instanceof i)
                        return r.apply(this, o),
                        this;
                    const s = new i(...o);
                    return a.annotation = s,
                    a;
                    function a(l, u, c) {
                        const d = l.hasOwnProperty($r) ? l[$r] : Object.defineProperty(l, $r, {
                            value: []
                        })[$r];
                        for (; d.length <= c; )
                            d.push(null);
                        return (d[c] = d[c] || []).push(s),
                        l
                    }
                }
                return t && (i.prototype = Object.create(t.prototype)),
                i.prototype.ngMetadataName = n,
                i.annotationCls = i,
                i
            }
            )
        }
        class S {
            constructor(e, t) {
                this._desc = e,
                this.ngMetadataName = "InjectionToken",
                this.\u0275prov = void 0,
                "number" == typeof t ? this.__NG_ELEMENT_ID__ = t : void 0 !== t && (this.\u0275prov = R({
                    token: this,
                    providedIn: t.providedIn || "root",
                    factory: t.factory
                }))
            }
            toString() {
                return `InjectionToken ${this._desc}`
            }
        }
        function Pt(n, e) {
            void 0 === e && (e = n);
            for (let t = 0; t < n.length; t++) {
                let r = n[t];
                Array.isArray(r) ? (e === n && (e = n.slice(0, t)),
                Pt(r, e)) : e !== n && e.push(r)
            }
            return e
        }
        function ln(n, e) {
            n.forEach(t=>Array.isArray(t) ? ln(t, e) : e(t))
        }
        function Lh(n, e, t) {
            e >= n.length ? n.push(t) : n.splice(e, 0, t)
        }
        function _s(n, e) {
            return e >= n.length - 1 ? n.pop() : n.splice(e, 1)[0]
        }
        function $i(n, e) {
            const t = [];
            for (let r = 0; r < n; r++)
                t.push(e);
            return t
        }
        function mt(n, e, t) {
            let r = qr(n, e);
            return r >= 0 ? n[1 | r] = t : (r = ~r,
            function QE(n, e, t, r) {
                let i = n.length;
                if (i == e)
                    n.push(t, r);
                else if (1 === i)
                    n.push(r, n[0]),
                    n[0] = t;
                else {
                    for (i--,
                    n.push(n[i - 1], n[i]); i > e; )
                        n[i] = n[i - 2],
                        i--;
                    n[e] = t,
                    n[e + 1] = r
                }
            }(n, r, e, t)),
            r
        }
        function Jl(n, e) {
            const t = qr(n, e);
            if (t >= 0)
                return n[1 | t]
        }
        function qr(n, e) {
            return function jh(n, e, t) {
                let r = 0
                  , i = n.length >> t;
                for (; i !== r; ) {
                    const o = r + (i - r >> 1)
                      , s = n[o << t];
                    if (e === s)
                        return o << t;
                    s > e ? i = o : r = o + 1
                }
                return ~(i << t)
            }(n, e, 1)
        }
        const Gi = {}
          , tu = "__NG_DI_FLAG__"
          , bs = "ngTempTokenPath"
          , nw = /\n/gm
          , Uh = "__source"
          , iw = re({
            provide: String,
            useValue: re
        });
        let zi;
        function $h(n) {
            const e = zi;
            return zi = n,
            e
        }
        function ow(n, e=H.Default) {
            if (void 0 === zi)
                throw new M(203,"");
            return null === zi ? th(n, void 0, e) : zi.get(n, e & H.Optional ? null : void 0, e)
        }
        function w(n, e=H.Default) {
            return (function GC() {
                return El
            }() || ow)(U(n), e)
        }
        const Ds = w;
        function nu(n) {
            const e = [];
            for (let t = 0; t < n.length; t++) {
                const r = U(n[t]);
                if (Array.isArray(r)) {
                    if (0 === r.length)
                        throw new M(900,"");
                    let i, o = H.Default;
                    for (let s = 0; s < r.length; s++) {
                        const a = r[s]
                          , l = sw(a);
                        "number" == typeof l ? -1 === l ? i = a.token : o |= l : i = a
                    }
                    e.push(w(i, o))
                } else
                    e.push(w(r))
            }
            return e
        }
        function qi(n, e) {
            return n[tu] = e,
            n.prototype[tu] = e,
            n
        }
        function sw(n) {
            return n[tu]
        }
        const ur = qi(zr("Optional"), 8)
          , Wi = qi(zr("SkipSelf"), 4);
        let Es;
        function Kr(n) {
            var e;
            return (null === (e = function ou() {
                if (void 0 === Es && (Es = null,
                ne.trustedTypes))
                    try {
                        Es = ne.trustedTypes.createPolicy("angular", {
                            createHTML: n=>n,
                            createScript: n=>n,
                            createScriptURL: n=>n
                        })
                    } catch (n) {}
                return Es
            }()) || void 0 === e ? void 0 : e.createHTML(n)) || n
        }
        class cr {
            constructor(e) {
                this.changingThisBreaksApplicationSecurity = e
            }
            toString() {
                return `SafeValue must use [property]=binding: ${this.changingThisBreaksApplicationSecurity} (see https://g.co/ng/security#xss)`
            }
        }
        class vw extends cr {
            getTypeName() {
                return "HTML"
            }
        }
        class bw extends cr {
            getTypeName() {
                return "Style"
            }
        }
        class Dw extends cr {
            getTypeName() {
                return "Script"
            }
        }
        class Cw extends cr {
            getTypeName() {
                return "URL"
            }
        }
        class Ew extends cr {
            getTypeName() {
                return "ResourceURL"
            }
        }
        function gt(n) {
            return n instanceof cr ? n.changingThisBreaksApplicationSecurity : n
        }
        function un(n, e) {
            const t = Xh(n);
            if (null != t && t !== e) {
                if ("ResourceURL" === t && "URL" === e)
                    return !0;
                throw new Error(`Required a safe ${e}, got a ${t} (see https://g.co/ng/security#xss)`)
            }
            return t === e
        }
        function Xh(n) {
            return n instanceof cr && n.getTypeName() || null
        }
        class Sw {
            constructor(e) {
                this.inertDocumentHelper = e
            }
            getInertBodyElement(e) {
                e = "<body><remove></remove>" + e;
                try {
                    const t = (new window.DOMParser).parseFromString(Kr(e), "text/html").body;
                    return null === t ? this.inertDocumentHelper.getInertBodyElement(e) : (t.removeChild(t.firstChild),
                    t)
                } catch (t) {
                    return null
                }
            }
        }
        class xw {
            constructor(e) {
                if (this.defaultDoc = e,
                this.inertDocument = this.defaultDoc.implementation.createHTMLDocument("sanitization-inert"),
                null == this.inertDocument.body) {
                    const t = this.inertDocument.createElement("html");
                    this.inertDocument.appendChild(t);
                    const r = this.inertDocument.createElement("body");
                    t.appendChild(r)
                }
            }
            getInertBodyElement(e) {
                const t = this.inertDocument.createElement("template");
                if ("content"in t)
                    return t.innerHTML = Kr(e),
                    t;
                const r = this.inertDocument.createElement("body");
                return r.innerHTML = Kr(e),
                this.defaultDoc.documentMode && this.stripCustomNsAttrs(r),
                r
            }
            stripCustomNsAttrs(e) {
                const t = e.attributes;
                for (let i = t.length - 1; 0 < i; i--) {
                    const s = t.item(i).name;
                    ("xmlns:ns1" === s || 0 === s.indexOf("ns1:")) && e.removeAttribute(s)
                }
                let r = e.firstChild;
                for (; r; )
                    r.nodeType === Node.ELEMENT_NODE && this.stripCustomNsAttrs(r),
                    r = r.nextSibling
            }
        }
        const Nw = /^(?:(?:https?|mailto|ftp|tel|file|sms):|[^&:/?#]*(?:[/?#]|$))/gi
          , Ow = /^data:(?:image\/(?:bmp|gif|jpeg|jpg|png|tiff|webp)|video\/(?:mpeg|mp4|ogg|webm)|audio\/(?:mp3|oga|ogg|opus));base64,[a-z0-9+\/]+=*$/i;
        function Qi(n) {
            return (n = String(n)).match(Nw) || n.match(Ow) ? n : "unsafe:" + n
        }
        function cn(n) {
            const e = {};
            for (const t of n.split(","))
                e[t] = !0;
            return e
        }
        function Zi(...n) {
            const e = {};
            for (const t of n)
                for (const r in t)
                    t.hasOwnProperty(r) && (e[r] = !0);
            return e
        }
        const tp = cn("area,br,col,hr,img,wbr")
          , np = cn("colgroup,dd,dt,li,p,tbody,td,tfoot,th,thead,tr")
          , rp = cn("rp,rt")
          , au = Zi(tp, Zi(np, cn("address,article,aside,blockquote,caption,center,del,details,dialog,dir,div,dl,figure,figcaption,footer,h1,h2,h3,h4,h5,h6,header,hgroup,hr,ins,main,map,menu,nav,ol,pre,section,summary,table,ul")), Zi(rp, cn("a,abbr,acronym,audio,b,bdi,bdo,big,br,cite,code,del,dfn,em,font,i,img,ins,kbd,label,map,mark,picture,q,ruby,rp,rt,s,samp,small,source,span,strike,strong,sub,sup,time,track,tt,u,var,video")), Zi(rp, np))
          , lu = cn("background,cite,href,itemtype,longdesc,poster,src,xlink:href")
          , uu = cn("srcset")
          , ip = Zi(lu, uu, cn("abbr,accesskey,align,alt,autoplay,axis,bgcolor,border,cellpadding,cellspacing,class,clear,color,cols,colspan,compact,controls,coords,datetime,default,dir,download,face,headers,height,hidden,hreflang,hspace,ismap,itemscope,itemprop,kind,label,lang,language,loop,media,muted,nohref,nowrap,open,preload,rel,rev,role,rows,rowspan,rules,scope,scrolling,shape,size,sizes,span,srclang,start,summary,tabindex,target,title,translate,type,usemap,valign,value,vspace,width"), cn("aria-activedescendant,aria-atomic,aria-autocomplete,aria-busy,aria-checked,aria-colcount,aria-colindex,aria-colspan,aria-controls,aria-current,aria-describedby,aria-details,aria-disabled,aria-dropeffect,aria-errormessage,aria-expanded,aria-flowto,aria-grabbed,aria-haspopup,aria-hidden,aria-invalid,aria-keyshortcuts,aria-label,aria-labelledby,aria-level,aria-live,aria-modal,aria-multiline,aria-multiselectable,aria-orientation,aria-owns,aria-placeholder,aria-posinset,aria-pressed,aria-readonly,aria-relevant,aria-required,aria-roledescription,aria-rowcount,aria-rowindex,aria-rowspan,aria-selected,aria-setsize,aria-sort,aria-valuemax,aria-valuemin,aria-valuenow,aria-valuetext"))
          , kw = cn("script,style,template");
        class Rw {
            constructor() {
                this.sanitizedSomething = !1,
                this.buf = []
            }
            sanitizeChildren(e) {
                let t = e.firstChild
                  , r = !0;
                for (; t; )
                    if (t.nodeType === Node.ELEMENT_NODE ? r = this.startElement(t) : t.nodeType === Node.TEXT_NODE ? this.chars(t.nodeValue) : this.sanitizedSomething = !0,
                    r && t.firstChild)
                        t = t.firstChild;
                    else
                        for (; t; ) {
                            t.nodeType === Node.ELEMENT_NODE && this.endElement(t);
                            let i = this.checkClobberedElement(t, t.nextSibling);
                            if (i) {
                                t = i;
                                break
                            }
                            t = this.checkClobberedElement(t, t.parentNode)
                        }
                return this.buf.join("")
            }
            startElement(e) {
                const t = e.nodeName.toLowerCase();
                if (!au.hasOwnProperty(t))
                    return this.sanitizedSomething = !0,
                    !kw.hasOwnProperty(t);
                this.buf.push("<"),
                this.buf.push(t);
                const r = e.attributes;
                for (let i = 0; i < r.length; i++) {
                    const o = r.item(i)
                      , s = o.name
                      , a = s.toLowerCase();
                    if (!ip.hasOwnProperty(a)) {
                        this.sanitizedSomething = !0;
                        continue
                    }
                    let l = o.value;
                    lu[a] && (l = Qi(l)),
                    uu[a] && (n = l,
                    l = (n = String(n)).split(",").map(e=>Qi(e.trim())).join(", ")),
                    this.buf.push(" ", s, '="', op(l), '"')
                }
                var n;
                return this.buf.push(">"),
                !0
            }
            endElement(e) {
                const t = e.nodeName.toLowerCase();
                au.hasOwnProperty(t) && !tp.hasOwnProperty(t) && (this.buf.push("</"),
                this.buf.push(t),
                this.buf.push(">"))
            }
            chars(e) {
                this.buf.push(op(e))
            }
            checkClobberedElement(e, t) {
                if (t && (e.compareDocumentPosition(t) & Node.DOCUMENT_POSITION_CONTAINED_BY) === Node.DOCUMENT_POSITION_CONTAINED_BY)
                    throw new Error(`Failed to sanitize html because the element is clobbered: ${e.outerHTML}`);
                return t
            }
        }
        const Pw = /[\uD800-\uDBFF][\uDC00-\uDFFF]/g
          , Lw = /([^\#-~ |!])/g;
        function op(n) {
            return n.replace(/&/g, "&amp;").replace(Pw, function(e) {
                return "&#" + (1024 * (e.charCodeAt(0) - 55296) + (e.charCodeAt(1) - 56320) + 65536) + ";"
            }).replace(Lw, function(e) {
                return "&#" + e.charCodeAt(0) + ";"
            }).replace(/</g, "&lt;").replace(/>/g, "&gt;")
        }
        let Ms;
        function sp(n, e) {
            let t = null;
            try {
                Ms = Ms || function Jh(n) {
                    const e = new xw(n);
                    return function Fw() {
                        try {
                            return !!(new window.DOMParser).parseFromString(Kr(""), "text/html")
                        } catch (n) {
                            return !1
                        }
                    }() ? new Sw(e) : e
                }(n);
                let r = e ? String(e) : "";
                t = Ms.getInertBodyElement(r);
                let i = 5
                  , o = r;
                do {
                    if (0 === i)
                        throw new Error("Failed to sanitize html because the input is unstable");
                    i--,
                    r = o,
                    o = t.innerHTML,
                    t = Ms.getInertBodyElement(r)
                } while (r !== o);
                return Kr((new Rw).sanitizeChildren(cu(t) || t))
            } finally {
                if (t) {
                    const r = cu(t) || t;
                    for (; r.firstChild; )
                        r.removeChild(r.firstChild)
                }
            }
        }
        function cu(n) {
            return "content"in n && function Vw(n) {
                return n.nodeType === Node.ELEMENT_NODE && "TEMPLATE" === n.nodeName
            }(n) ? n.content : null
        }
        var ee = (()=>((ee = ee || {})[ee.NONE = 0] = "NONE",
        ee[ee.HTML = 1] = "HTML",
        ee[ee.STYLE = 2] = "STYLE",
        ee[ee.SCRIPT = 3] = "SCRIPT",
        ee[ee.URL = 4] = "URL",
        ee[ee.RESOURCE_URL = 5] = "RESOURCE_URL",
        ee))();
        function As(n) {
            const e = function Yi() {
                const n = b();
                return n && n[12]
            }();
            return e ? e.sanitize(ee.URL, n) || "" : un(n, "URL") ? gt(n) : Qi(L(n))
        }
        const up = "__ngContext__";
        function qe(n, e) {
            n[up] = e
        }
        function fu(n) {
            const e = function Xi(n) {
                return n[up] || null
            }(n);
            return e ? Array.isArray(e) ? e : e.lView : null
        }
        function pu(n) {
            return n.ngOriginalError
        }
        function t0(n, ...e) {
            n.error(...e)
        }
        class Hn {
            constructor() {
                this._console = console
            }
            handleError(e) {
                const t = this._findOriginalError(e)
                  , r = function e0(n) {
                    return n && n.ngErrorLogger || t0
                }(e);
                r(this._console, "ERROR", e),
                t && r(this._console, "ORIGINAL ERROR", t)
            }
            _findOriginalError(e) {
                let t = e && pu(e);
                for (; t && pu(t); )
                    t = pu(t);
                return t || null
            }
        }
        const f0 = (()=>("undefined" != typeof requestAnimationFrame && requestAnimationFrame || setTimeout).bind(ne))();
        function dn(n) {
            return n instanceof Function ? n() : n
        }
        var yt = (()=>((yt = yt || {})[yt.Important = 1] = "Important",
        yt[yt.DashCase = 2] = "DashCase",
        yt))();
        function gu(n, e) {
            return undefined(n, e)
        }
        function Ji(n) {
            const e = n[3];
            return qt(e) ? e[3] : e
        }
        function yu(n) {
            return _p(n[13])
        }
        function _u(n) {
            return _p(n[4])
        }
        function _p(n) {
            for (; null !== n && !qt(n); )
                n = n[4];
            return n
        }
        function Zr(n, e, t, r, i) {
            if (null != r) {
                let o, s = !1;
                qt(r) ? o = r : on(r) && (s = !0,
                r = r[0]);
                const a = Te(r);
                0 === n && null !== t ? null == i ? wp(e, t, a) : dr(e, t, a, i || null, !0) : 1 === n && null !== t ? dr(e, t, a, i || null, !0) : 2 === n ? function Fp(n, e, t) {
                    const r = Ts(n, e);
                    r && function A0(n, e, t, r) {
                        Ce(n) ? n.removeChild(e, t, r) : e.removeChild(t)
                    }(n, r, e, t)
                }(e, a, s) : 3 === n && e.destroyNode(a),
                null != o && function S0(n, e, t, r, i) {
                    const o = t[7];
                    o !== Te(t) && Zr(e, n, r, o, i);
                    for (let a = 10; a < t.length; a++) {
                        const l = t[a];
                        eo(l[1], l, n, e, r, o)
                    }
                }(e, n, o, t, i)
            }
        }
        function bu(n, e, t) {
            if (Ce(n))
                return n.createElement(e, t);
            {
                const r = null !== t ? function cE(n) {
                    const e = n.toLowerCase();
                    return "svg" === e ? "http://www.w3.org/2000/svg" : "math" === e ? "http://www.w3.org/1998/MathML/" : null
                }(t) : null;
                return null === r ? n.createElement(e) : n.createElementNS(r, e)
            }
        }
        function bp(n, e) {
            const t = n[9]
              , r = t.indexOf(e)
              , i = e[3];
            1024 & e[2] && (e[2] &= -1025,
            Ll(i, -1)),
            t.splice(r, 1)
        }
        function Du(n, e) {
            if (n.length <= 10)
                return;
            const t = 10 + e
              , r = n[t];
            if (r) {
                const i = r[17];
                null !== i && i !== n && bp(i, r),
                e > 0 && (n[t - 1][4] = r[4]);
                const o = _s(n, 10 + e);
                !function _0(n, e) {
                    eo(n, e, e[$], 2, null, null),
                    e[0] = null,
                    e[6] = null
                }(r[1], r);
                const s = o[19];
                null !== s && s.detachView(o[1]),
                r[3] = null,
                r[4] = null,
                r[2] &= -129
            }
            return r
        }
        function Dp(n, e) {
            if (!(256 & e[2])) {
                const t = e[$];
                Ce(t) && t.destroyNode && eo(n, e, t, 3, null, null),
                function D0(n) {
                    let e = n[13];
                    if (!e)
                        return Cu(n[1], n);
                    for (; e; ) {
                        let t = null;
                        if (on(e))
                            t = e[13];
                        else {
                            const r = e[10];
                            r && (t = r)
                        }
                        if (!t) {
                            for (; e && !e[4] && e !== n; )
                                on(e) && Cu(e[1], e),
                                e = e[3];
                            null === e && (e = n),
                            on(e) && Cu(e[1], e),
                            t = e && e[4]
                        }
                        e = t
                    }
                }(e)
            }
        }
        function Cu(n, e) {
            if (!(256 & e[2])) {
                e[2] &= -129,
                e[2] |= 256,
                function M0(n, e) {
                    let t;
                    if (null != n && null != (t = n.destroyHooks))
                        for (let r = 0; r < t.length; r += 2) {
                            const i = e[t[r]];
                            if (!(i instanceof Li)) {
                                const o = t[r + 1];
                                if (Array.isArray(o))
                                    for (let s = 0; s < o.length; s += 2) {
                                        const a = i[o[s]]
                                          , l = o[s + 1];
                                        try {
                                            l.call(a)
                                        } finally {}
                                    }
                                else
                                    try {
                                        o.call(i)
                                    } finally {}
                            }
                        }
                }(n, e),
                function w0(n, e) {
                    const t = n.cleanup
                      , r = e[7];
                    let i = -1;
                    if (null !== t)
                        for (let o = 0; o < t.length - 1; o += 2)
                            if ("string" == typeof t[o]) {
                                const s = t[o + 1]
                                  , a = "function" == typeof s ? s(e) : Te(e[s])
                                  , l = r[i = t[o + 2]]
                                  , u = t[o + 3];
                                "boolean" == typeof u ? a.removeEventListener(t[o], l, u) : u >= 0 ? r[i = u]() : r[i = -u].unsubscribe(),
                                o += 2
                            } else {
                                const s = r[i = t[o + 1]];
                                t[o].call(s)
                            }
                    if (null !== r) {
                        for (let o = i + 1; o < r.length; o++)
                            r[o]();
                        e[7] = null
                    }
                }(n, e),
                1 === e[1].type && Ce(e[$]) && e[$].destroy();
                const t = e[17];
                if (null !== t && qt(e[3])) {
                    t !== e[3] && bp(t, e);
                    const r = e[19];
                    null !== r && r.detachView(n)
                }
            }
        }
        function Cp(n, e, t) {
            return function Ep(n, e, t) {
                let r = e;
                for (; null !== r && 40 & r.type; )
                    r = (e = r).parent;
                if (null === r)
                    return t[0];
                if (2 & r.flags) {
                    const i = n.data[r.directiveStart].encapsulation;
                    if (i === Gt.None || i === Gt.Emulated)
                        return null
                }
                return Rt(r, t)
            }(n, e.parent, t)
        }
        function dr(n, e, t, r, i) {
            Ce(n) ? n.insertBefore(e, t, r, i) : e.insertBefore(t, r, i)
        }
        function wp(n, e, t) {
            Ce(n) ? n.appendChild(e, t) : e.appendChild(t)
        }
        function Mp(n, e, t, r, i) {
            null !== r ? dr(n, e, t, r, i) : wp(n, e, t)
        }
        function Ts(n, e) {
            return Ce(n) ? n.parentNode(e) : e.parentNode
        }
        function Ap(n, e, t) {
            return Ip(n, e, t)
        }
        let Ip = function Tp(n, e, t) {
            return 40 & n.type ? Rt(n, t) : null
        };
        function Is(n, e, t, r) {
            const i = Cp(n, r, e)
              , o = e[$]
              , a = Ap(r.parent || e[6], r, e);
            if (null != i)
                if (Array.isArray(t))
                    for (let l = 0; l < t.length; l++)
                        Mp(o, i, t[l], a, !1);
                else
                    Mp(o, i, t, a, !1)
        }
        function Ss(n, e) {
            if (null !== e) {
                const t = e.type;
                if (3 & t)
                    return Rt(e, n);
                if (4 & t)
                    return wu(-1, n[e.index]);
                if (8 & t) {
                    const r = e.child;
                    if (null !== r)
                        return Ss(n, r);
                    {
                        const i = n[e.index];
                        return qt(i) ? wu(-1, i) : Te(i)
                    }
                }
                if (32 & t)
                    return gu(e, n)() || Te(n[e.index]);
                {
                    const r = xp(n, e);
                    return null !== r ? Array.isArray(r) ? r[0] : Ss(Ji(n[16]), r) : Ss(n, e.next)
                }
            }
            return null
        }
        function xp(n, e) {
            return null !== e ? n[16][6].projection[e.projection] : null
        }
        function wu(n, e) {
            const t = 10 + n + 1;
            if (t < e.length) {
                const r = e[t]
                  , i = r[1].firstChild;
                if (null !== i)
                    return Ss(r, i)
            }
            return e[7]
        }
        function Mu(n, e, t, r, i, o, s) {
            for (; null != t; ) {
                const a = r[t.index]
                  , l = t.type;
                if (s && 0 === e && (a && qe(Te(a), r),
                t.flags |= 4),
                64 != (64 & t.flags))
                    if (8 & l)
                        Mu(n, e, t.child, r, i, o, !1),
                        Zr(e, n, i, a, o);
                    else if (32 & l) {
                        const u = gu(t, r);
                        let c;
                        for (; c = u(); )
                            Zr(e, n, i, c, o);
                        Zr(e, n, i, a, o)
                    } else
                        16 & l ? Np(n, e, r, t, i, o) : Zr(e, n, i, a, o);
                t = s ? t.projectionNext : t.next
            }
        }
        function eo(n, e, t, r, i, o) {
            Mu(t, r, n.firstChild, e, i, o, !1)
        }
        function Np(n, e, t, r, i, o) {
            const s = t[16]
              , l = s[6].projection[r.projection];
            if (Array.isArray(l))
                for (let u = 0; u < l.length; u++)
                    Zr(e, n, i, l[u], o);
            else
                Mu(n, e, l, s[3], i, o, !0)
        }
        function Op(n, e, t) {
            Ce(n) ? n.setAttribute(e, "style", t) : e.style.cssText = t
        }
        function Au(n, e, t) {
            Ce(n) ? "" === t ? n.removeAttribute(e, "class") : n.setAttribute(e, "class", t) : e.className = t
        }
        function kp(n, e, t) {
            let r = n.length;
            for (; ; ) {
                const i = n.indexOf(e, t);
                if (-1 === i)
                    return i;
                if (0 === i || n.charCodeAt(i - 1) <= 32) {
                    const o = e.length;
                    if (i + o === r || n.charCodeAt(i + o) <= 32)
                        return i
                }
                t = i + 1
            }
        }
        const Rp = "ng-template";
        function F0(n, e, t) {
            let r = 0;
            for (; r < n.length; ) {
                let i = n[r++];
                if (t && "class" === i) {
                    if (i = n[r],
                    -1 !== kp(i.toLowerCase(), e, 0))
                        return !0
                } else if (1 === i) {
                    for (; r < n.length && "string" == typeof (i = n[r++]); )
                        if (i.toLowerCase() === e)
                            return !0;
                    return !1
                }
            }
            return !1
        }
        function Pp(n) {
            return 4 === n.type && n.value !== Rp
        }
        function N0(n, e, t) {
            return e === (4 !== n.type || t ? n.value : Rp)
        }
        function O0(n, e, t) {
            let r = 4;
            const i = n.attrs || []
              , o = function P0(n) {
                for (let e = 0; e < n.length; e++)
                    if (Mh(n[e]))
                        return e;
                return n.length
            }(i);
            let s = !1;
            for (let a = 0; a < e.length; a++) {
                const l = e[a];
                if ("number" != typeof l) {
                    if (!s)
                        if (4 & r) {
                            if (r = 2 | 1 & r,
                            "" !== l && !N0(n, l, t) || "" === l && 1 === e.length) {
                                if (Kt(r))
                                    return !1;
                                s = !0
                            }
                        } else {
                            const u = 8 & r ? l : e[++a];
                            if (8 & r && null !== n.attrs) {
                                if (!F0(n.attrs, u, t)) {
                                    if (Kt(r))
                                        return !1;
                                    s = !0
                                }
                                continue
                            }
                            const d = k0(8 & r ? "class" : l, i, Pp(n), t);
                            if (-1 === d) {
                                if (Kt(r))
                                    return !1;
                                s = !0;
                                continue
                            }
                            if ("" !== u) {
                                let f;
                                f = d > o ? "" : i[d + 1].toLowerCase();
                                const h = 8 & r ? f : null;
                                if (h && -1 !== kp(h, u, 0) || 2 & r && u !== f) {
                                    if (Kt(r))
                                        return !1;
                                    s = !0
                                }
                            }
                        }
                } else {
                    if (!s && !Kt(r) && !Kt(l))
                        return !1;
                    if (s && Kt(l))
                        continue;
                    s = !1,
                    r = l | 1 & r
                }
            }
            return Kt(r) || s
        }
        function Kt(n) {
            return 0 == (1 & n)
        }
        function k0(n, e, t, r) {
            if (null === e)
                return -1;
            let i = 0;
            if (r || !t) {
                let o = !1;
                for (; i < e.length; ) {
                    const s = e[i];
                    if (s === n)
                        return i;
                    if (3 === s || 6 === s)
                        o = !0;
                    else {
                        if (1 === s || 2 === s) {
                            let a = e[++i];
                            for (; "string" == typeof a; )
                                a = e[++i];
                            continue
                        }
                        if (4 === s)
                            break;
                        if (0 === s) {
                            i += 4;
                            continue
                        }
                    }
                    i += o ? 1 : 2
                }
                return -1
            }
            return function L0(n, e) {
                let t = n.indexOf(4);
                if (t > -1)
                    for (t++; t < n.length; ) {
                        const r = n[t];
                        if ("number" == typeof r)
                            return -1;
                        if (r === e)
                            return t;
                        t++
                    }
                return -1
            }(e, n)
        }
        function Lp(n, e, t=!1) {
            for (let r = 0; r < e.length; r++)
                if (O0(n, e[r], t))
                    return !0;
            return !1
        }
        function V0(n, e) {
            e: for (let t = 0; t < e.length; t++) {
                const r = e[t];
                if (n.length === r.length) {
                    for (let i = 0; i < n.length; i++)
                        if (n[i] !== r[i])
                            continue e;
                    return !0
                }
            }
            return !1
        }
        function Vp(n, e) {
            return n ? ":not(" + e.trim() + ")" : e
        }
        function B0(n) {
            let e = n[0]
              , t = 1
              , r = 2
              , i = ""
              , o = !1;
            for (; t < n.length; ) {
                let s = n[t];
                if ("string" == typeof s)
                    if (2 & r) {
                        const a = n[++t];
                        i += "[" + s + (a.length > 0 ? '="' + a + '"' : "") + "]"
                    } else
                        8 & r ? i += "." + s : 4 & r && (i += " " + s);
                else
                    "" !== i && !Kt(s) && (e += Vp(o, i),
                    i = ""),
                    r = s,
                    o = o || !Kt(r);
                t++
            }
            return "" !== i && (e += Vp(o, i)),
            e
        }
        const V = {};
        function de(n) {
            Bp(Q(), b(), Ye() + n, is())
        }
        function Bp(n, e, t, r) {
            if (!r)
                if (3 == (3 & e[2])) {
                    const o = n.preOrderCheckHooks;
                    null !== o && us(e, o, t)
                } else {
                    const o = n.preOrderHooks;
                    null !== o && cs(e, o, 0, t)
                }
            Bn(t)
        }
        function xs(n, e) {
            return n << 17 | e << 2
        }
        function Qt(n) {
            return n >> 17 & 32767
        }
        function Tu(n) {
            return 2 | n
        }
        function Mn(n) {
            return (131068 & n) >> 2
        }
        function Iu(n, e) {
            return -131069 & n | e << 2
        }
        function Su(n) {
            return 1 | n
        }
        function Zp(n, e) {
            const t = n.contentQueries;
            if (null !== t)
                for (let r = 0; r < t.length; r += 2) {
                    const i = t[r]
                      , o = t[r + 1];
                    if (-1 !== o) {
                        const s = n.data[o];
                        $l(i),
                        s.contentQueries(2, e[o], o)
                    }
                }
        }
        function to(n, e, t, r, i, o, s, a, l, u) {
            const c = e.blueprint.slice();
            return c[0] = i,
            c[2] = 140 | r,
            hh(c),
            c[3] = c[15] = n,
            c[8] = t,
            c[10] = s || n && n[10],
            c[$] = a || n && n[$],
            c[12] = l || n && n[12] || null,
            c[9] = u || n && n[9] || null,
            c[6] = o,
            c[16] = 2 == e.type ? n[16] : c,
            c
        }
        function Yr(n, e, t, r, i) {
            let o = n.data[e];
            if (null === o)
                o = function Vu(n, e, t, r, i) {
                    const o = mh()
                      , s = Bl()
                      , l = n.data[e] = function rM(n, e, t, r, i, o) {
                        return {
                            type: t,
                            index: r,
                            insertBeforeIndex: null,
                            injectorIndex: e ? e.injectorIndex : -1,
                            directiveStart: -1,
                            directiveEnd: -1,
                            directiveStylingLast: -1,
                            propertyBindings: null,
                            flags: 0,
                            providerIndexes: 0,
                            value: i,
                            attrs: o,
                            mergedAttrs: null,
                            localNames: null,
                            initialInputs: void 0,
                            inputs: null,
                            outputs: null,
                            tViews: null,
                            next: null,
                            projectionNext: null,
                            child: null,
                            parent: e,
                            projection: null,
                            styles: null,
                            stylesWithoutHost: null,
                            residualStyles: void 0,
                            classes: null,
                            classesWithoutHost: null,
                            residualClasses: void 0,
                            classBindings: 0,
                            styleBindings: 0
                        }
                    }(0, s ? o : o && o.parent, t, e, r, i);
                    return null === n.firstChild && (n.firstChild = l),
                    null !== o && (s ? null == o.child && null !== l.parent && (o.child = l) : null === o.next && (o.next = l)),
                    l
                }(n, e, t, r, i),
                function CE() {
                    return P.lFrame.inI18n
                }() && (o.flags |= 64);
            else if (64 & o.type) {
                o.type = t,
                o.value = r,
                o.attrs = i;
                const s = function Pi() {
                    const n = P.lFrame
                      , e = n.currentTNode;
                    return n.isParent ? e : e.parent
                }();
                o.injectorIndex = null === s ? -1 : s.injectorIndex
            }
            return an(o, !0),
            o
        }
        function Xr(n, e, t, r) {
            if (0 === t)
                return -1;
            const i = e.length;
            for (let o = 0; o < t; o++)
                e.push(r),
                n.blueprint.push(r),
                n.data.push(null);
            return i
        }
        function no(n, e, t) {
            ss(e);
            try {
                const r = n.viewQuery;
                null !== r && Wu(1, r, t);
                const i = n.template;
                null !== i && Yp(n, e, i, 1, t),
                n.firstCreatePass && (n.firstCreatePass = !1),
                n.staticContentQueries && Zp(n, e),
                n.staticViewQueries && Wu(2, n.viewQuery, t);
                const o = n.components;
                null !== o && function eM(n, e) {
                    for (let t = 0; t < e.length; t++)
                        DM(n, e[t])
                }(e, o)
            } catch (r) {
                throw n.firstCreatePass && (n.incompleteFirstPass = !0,
                n.firstCreatePass = !1),
                r
            } finally {
                e[2] &= -5,
                as()
            }
        }
        function Jr(n, e, t, r) {
            const i = e[2];
            if (256 == (256 & i))
                return;
            ss(e);
            const o = is();
            try {
                hh(e),
                function gh(n) {
                    return P.lFrame.bindingIndex = n
                }(n.bindingStartIndex),
                null !== t && Yp(n, e, t, 2, r);
                const s = 3 == (3 & i);
                if (!o)
                    if (s) {
                        const u = n.preOrderCheckHooks;
                        null !== u && us(e, u, null)
                    } else {
                        const u = n.preOrderHooks;
                        null !== u && cs(e, u, 0, null),
                        Gl(e, 0)
                    }
                if (function vM(n) {
                    for (let e = yu(n); null !== e; e = _u(e)) {
                        if (!e[2])
                            continue;
                        const t = e[9];
                        for (let r = 0; r < t.length; r++) {
                            const i = t[r]
                              , o = i[3];
                            0 == (1024 & i[2]) && Ll(o, 1),
                            i[2] |= 1024
                        }
                    }
                }(e),
                function _M(n) {
                    for (let e = yu(n); null !== e; e = _u(e))
                        for (let t = 10; t < e.length; t++) {
                            const r = e[t]
                              , i = r[1];
                            Pl(r) && Jr(i, r, i.template, r[8])
                        }
                }(e),
                null !== n.contentQueries && Zp(n, e),
                !o)
                    if (s) {
                        const u = n.contentCheckHooks;
                        null !== u && us(e, u)
                    } else {
                        const u = n.contentHooks;
                        null !== u && cs(e, u, 1),
                        Gl(e, 1)
                    }
                !function X0(n, e) {
                    const t = n.hostBindingOpCodes;
                    if (null !== t)
                        try {
                            for (let r = 0; r < t.length; r++) {
                                const i = t[r];
                                if (i < 0)
                                    Bn(~i);
                                else {
                                    const o = i
                                      , s = t[++r]
                                      , a = t[++r];
                                    EE(s, o),
                                    a(2, e[o])
                                }
                            }
                        } finally {
                            Bn(-1)
                        }
                }(n, e);
                const a = n.components;
                null !== a && function J0(n, e) {
                    for (let t = 0; t < e.length; t++)
                        bM(n, e[t])
                }(e, a);
                const l = n.viewQuery;
                if (null !== l && Wu(2, l, r),
                !o)
                    if (s) {
                        const u = n.viewCheckHooks;
                        null !== u && us(e, u)
                    } else {
                        const u = n.viewHooks;
                        null !== u && cs(e, u, 2),
                        Gl(e, 2)
                    }
                !0 === n.firstUpdatePass && (n.firstUpdatePass = !1),
                o || (e[2] &= -73),
                1024 & e[2] && (e[2] &= -1025,
                Ll(e[3], -1))
            } finally {
                as()
            }
        }
        function tM(n, e, t, r) {
            const i = e[10]
              , o = !is()
              , s = fh(e);
            try {
                o && !s && i.begin && i.begin(),
                s && no(n, e, r),
                Jr(n, e, t, r)
            } finally {
                o && !s && i.end && i.end()
            }
        }
        function Yp(n, e, t, r, i) {
            const o = Ye()
              , s = 2 & r;
            try {
                Bn(-1),
                s && e.length > 20 && Bp(n, e, 20, is()),
                t(r, i)
            } finally {
                Bn(o)
            }
        }
        function Xp(n, e, t) {
            if (Il(e)) {
                const i = e.directiveEnd;
                for (let o = e.directiveStart; o < i; o++) {
                    const s = n.data[o];
                    s.contentQueries && s.contentQueries(1, t[o], o)
                }
            }
        }
        function Bu(n, e, t) {
            !ph() || (function cM(n, e, t, r) {
                const i = t.directiveStart
                  , o = t.directiveEnd;
                n.firstCreatePass || Bi(t, e),
                qe(r, e);
                const s = t.initialInputs;
                for (let a = i; a < o; a++) {
                    const l = n.data[a]
                      , u = Wt(l);
                    u && mM(e, t, l);
                    const c = ji(e, n, a, t);
                    qe(c, e),
                    null !== s && gM(0, a - i, c, l, 0, s),
                    u && (pt(t.index, e)[8] = c)
                }
            }(n, e, t, Rt(t, e)),
            128 == (128 & t.flags) && function dM(n, e, t) {
                const r = t.directiveStart
                  , i = t.directiveEnd
                  , s = t.index
                  , a = function wE() {
                    return P.lFrame.currentDirectiveIndex
                }();
                try {
                    Bn(s);
                    for (let l = r; l < i; l++) {
                        const u = n.data[l]
                          , c = e[l];
                        Hl(l),
                        (null !== u.hostBindings || 0 !== u.hostVars || null !== u.hostAttrs) && sm(u, c)
                    }
                } finally {
                    Bn(-1),
                    Hl(a)
                }
            }(n, e, t))
        }
        function ju(n, e, t=Rt) {
            const r = e.localNames;
            if (null !== r) {
                let i = e.index + 1;
                for (let o = 0; o < r.length; o += 2) {
                    const s = r[o + 1]
                      , a = -1 === s ? t(e, n) : n[s];
                    n[i++] = a
                }
            }
        }
        function Jp(n) {
            const e = n.tView;
            return null === e || e.incompleteFirstPass ? n.tView = Os(1, null, n.template, n.decls, n.vars, n.directiveDefs, n.pipeDefs, n.viewQuery, n.schemas, n.consts) : e
        }
        function Os(n, e, t, r, i, o, s, a, l, u) {
            const c = 20 + r
              , d = c + i
              , f = function nM(n, e) {
                const t = [];
                for (let r = 0; r < e; r++)
                    t.push(r < n ? null : V);
                return t
            }(c, d)
              , h = "function" == typeof u ? u() : u;
            return f[1] = {
                type: n,
                blueprint: f,
                template: t,
                queries: null,
                viewQuery: a,
                declTNode: e,
                data: f.slice().fill(null, c),
                bindingStartIndex: c,
                expandoStartIndex: d,
                hostBindingOpCodes: null,
                firstCreatePass: !0,
                firstUpdatePass: !0,
                staticViewQueries: !1,
                staticContentQueries: !1,
                preOrderHooks: null,
                preOrderCheckHooks: null,
                contentHooks: null,
                contentCheckHooks: null,
                viewHooks: null,
                viewCheckHooks: null,
                destroyHooks: null,
                cleanup: null,
                contentQueries: null,
                components: null,
                directiveRegistry: "function" == typeof o ? o() : o,
                pipeRegistry: "function" == typeof s ? s() : s,
                firstChild: null,
                schemas: l,
                consts: h,
                incompleteFirstPass: !1
            }
        }
        function nm(n, e, t, r) {
            const i = fm(e);
            null === t ? i.push(r) : (i.push(t),
            n.firstCreatePass && hm(n).push(r, i.length - 1))
        }
        function rm(n, e, t) {
            for (let r in n)
                if (n.hasOwnProperty(r)) {
                    const i = n[r];
                    (t = null === t ? {} : t).hasOwnProperty(r) ? t[r].push(e, i) : t[r] = [e, i]
                }
            return t
        }
        function _t(n, e, t, r, i, o, s, a) {
            const l = Rt(e, t);
            let c, u = e.inputs;
            !a && null != u && (c = u[r]) ? (gm(n, t, c, r, i),
            ts(e) && function sM(n, e) {
                const t = pt(e, n);
                16 & t[2] || (t[2] |= 64)
            }(t, e.index)) : 3 & e.type && (r = function oM(n) {
                return "class" === n ? "className" : "for" === n ? "htmlFor" : "formaction" === n ? "formAction" : "innerHtml" === n ? "innerHTML" : "readonly" === n ? "readOnly" : "tabindex" === n ? "tabIndex" : n
            }(r),
            i = null != s ? s(i, e.value || "", r) : i,
            Ce(o) ? o.setProperty(l, r, i) : ql(r) || (l.setProperty ? l.setProperty(r, i) : l[r] = i))
        }
        function Hu(n, e, t, r) {
            let i = !1;
            if (ph()) {
                const o = function fM(n, e, t) {
                    const r = n.directiveRegistry;
                    let i = null;
                    if (r)
                        for (let o = 0; o < r.length; o++) {
                            const s = r[o];
                            Lp(t, s.selectors, !1) && (i || (i = []),
                            ms(Bi(t, e), n, s.type),
                            Wt(s) ? (am(n, t),
                            i.unshift(s)) : i.push(s))
                        }
                    return i
                }(n, e, t)
                  , s = null === r ? null : {
                    "": -1
                };
                if (null !== o) {
                    i = !0,
                    lm(t, n.data.length, o.length);
                    for (let c = 0; c < o.length; c++) {
                        const d = o[c];
                        d.providersResolver && d.providersResolver(d)
                    }
                    let a = !1
                      , l = !1
                      , u = Xr(n, e, o.length, null);
                    for (let c = 0; c < o.length; c++) {
                        const d = o[c];
                        t.mergedAttrs = fs(t.mergedAttrs, d.hostAttrs),
                        um(n, t, e, u, d),
                        pM(u, d, s),
                        null !== d.contentQueries && (t.flags |= 8),
                        (null !== d.hostBindings || null !== d.hostAttrs || 0 !== d.hostVars) && (t.flags |= 128);
                        const f = d.type.prototype;
                        !a && (f.ngOnChanges || f.ngOnInit || f.ngDoCheck) && ((n.preOrderHooks || (n.preOrderHooks = [])).push(t.index),
                        a = !0),
                        !l && (f.ngOnChanges || f.ngDoCheck) && ((n.preOrderCheckHooks || (n.preOrderCheckHooks = [])).push(t.index),
                        l = !0),
                        u++
                    }
                    !function iM(n, e) {
                        const r = e.directiveEnd
                          , i = n.data
                          , o = e.attrs
                          , s = [];
                        let a = null
                          , l = null;
                        for (let u = e.directiveStart; u < r; u++) {
                            const c = i[u]
                              , d = c.inputs
                              , f = null === o || Pp(e) ? null : yM(d, o);
                            s.push(f),
                            a = rm(d, u, a),
                            l = rm(c.outputs, u, l)
                        }
                        null !== a && (a.hasOwnProperty("class") && (e.flags |= 16),
                        a.hasOwnProperty("style") && (e.flags |= 32)),
                        e.initialInputs = s,
                        e.inputs = a,
                        e.outputs = l
                    }(n, t)
                }
                s && function hM(n, e, t) {
                    if (e) {
                        const r = n.localNames = [];
                        for (let i = 0; i < e.length; i += 2) {
                            const o = t[e[i + 1]];
                            if (null == o)
                                throw new M(-301,!1);
                            r.push(e[i], o)
                        }
                    }
                }(t, r, s)
            }
            return t.mergedAttrs = fs(t.mergedAttrs, t.attrs),
            i
        }
        function om(n, e, t, r, i, o) {
            const s = o.hostBindings;
            if (s) {
                let a = n.hostBindingOpCodes;
                null === a && (a = n.hostBindingOpCodes = []);
                const l = ~e.index;
                (function uM(n) {
                    let e = n.length;
                    for (; e > 0; ) {
                        const t = n[--e];
                        if ("number" == typeof t && t < 0)
                            return t
                    }
                    return 0
                }
                )(a) != l && a.push(l),
                a.push(r, i, s)
            }
        }
        function sm(n, e) {
            null !== n.hostBindings && n.hostBindings(1, e)
        }
        function am(n, e) {
            e.flags |= 2,
            (n.components || (n.components = [])).push(e.index)
        }
        function pM(n, e, t) {
            if (t) {
                if (e.exportAs)
                    for (let r = 0; r < e.exportAs.length; r++)
                        t[e.exportAs[r]] = n;
                Wt(e) && (t[""] = n)
            }
        }
        function lm(n, e, t) {
            n.flags |= 1,
            n.directiveStart = e,
            n.directiveEnd = e + t,
            n.providerIndexes = e
        }
        function um(n, e, t, r, i) {
            n.data[r] = i;
            const o = i.factory || (i.factory = lr(i.type))
              , s = new Li(o,Wt(i),null);
            n.blueprint[r] = s,
            t[r] = s,
            om(n, e, 0, r, Xr(n, t, i.hostVars, V), i)
        }
        function mM(n, e, t) {
            const r = Rt(e, n)
              , i = Jp(t)
              , o = n[10]
              , s = ks(n, to(n, i, null, t.onPush ? 64 : 16, r, e, o, o.createRenderer(r, t), null, null));
            n[e.index] = s
        }
        function fn(n, e, t, r, i, o) {
            const s = Rt(n, e);
            !function Uu(n, e, t, r, i, o, s) {
                if (null == o)
                    Ce(n) ? n.removeAttribute(e, i, t) : e.removeAttribute(i);
                else {
                    const a = null == s ? L(o) : s(o, r || "", i);
                    Ce(n) ? n.setAttribute(e, i, a, t) : t ? e.setAttributeNS(t, i, a) : e.setAttribute(i, a)
                }
            }(e[$], s, o, n.value, t, r, i)
        }
        function gM(n, e, t, r, i, o) {
            const s = o[e];
            if (null !== s) {
                const a = r.setInput;
                for (let l = 0; l < s.length; ) {
                    const u = s[l++]
                      , c = s[l++]
                      , d = s[l++];
                    null !== a ? r.setInput(t, d, u, c) : t[c] = d
                }
            }
        }
        function yM(n, e) {
            let t = null
              , r = 0;
            for (; r < e.length; ) {
                const i = e[r];
                if (0 !== i)
                    if (5 !== i) {
                        if ("number" == typeof i)
                            break;
                        n.hasOwnProperty(i) && (null === t && (t = []),
                        t.push(i, n[i], e[r + 1])),
                        r += 2
                    } else
                        r += 2;
                else
                    r += 4
            }
            return t
        }
        function cm(n, e, t, r) {
            return new Array(n,!0,!1,e,null,0,r,t,null,null)
        }
        function bM(n, e) {
            const t = pt(e, n);
            if (Pl(t)) {
                const r = t[1];
                80 & t[2] ? Jr(r, t, r.template, t[8]) : t[5] > 0 && $u(t)
            }
        }
        function $u(n) {
            for (let r = yu(n); null !== r; r = _u(r))
                for (let i = 10; i < r.length; i++) {
                    const o = r[i];
                    if (1024 & o[2]) {
                        const s = o[1];
                        Jr(s, o, s.template, o[8])
                    } else
                        o[5] > 0 && $u(o)
                }
            const t = n[1].components;
            if (null !== t)
                for (let r = 0; r < t.length; r++) {
                    const i = pt(t[r], n);
                    Pl(i) && i[5] > 0 && $u(i)
                }
        }
        function DM(n, e) {
            const t = pt(e, n)
              , r = t[1];
            (function CM(n, e) {
                for (let t = e.length; t < n.blueprint.length; t++)
                    e.push(n.blueprint[t])
            }
            )(r, t),
            no(r, t, t[8])
        }
        function ks(n, e) {
            return n[13] ? n[14][4] = e : n[13] = e,
            n[14] = e,
            e
        }
        function Gu(n) {
            for (; n; ) {
                n[2] |= 64;
                const e = Ji(n);
                if (eE(n) && !e)
                    return n;
                n = e
            }
            return null
        }
        function qu(n, e, t) {
            const r = e[10];
            r.begin && r.begin();
            try {
                Jr(n, e, n.template, t)
            } catch (i) {
                throw mm(e, i),
                i
            } finally {
                r.end && r.end()
            }
        }
        function dm(n) {
            !function zu(n) {
                for (let e = 0; e < n.components.length; e++) {
                    const t = n.components[e]
                      , r = fu(t)
                      , i = r[1];
                    tM(i, r, i.template, t)
                }
            }(n[8])
        }
        function Wu(n, e, t) {
            $l(0),
            e(n, t)
        }
        const AM = (()=>Promise.resolve(null))();
        function fm(n) {
            return n[7] || (n[7] = [])
        }
        function hm(n) {
            return n.cleanup || (n.cleanup = [])
        }
        function mm(n, e) {
            const t = n[9]
              , r = t ? t.get(Hn, null) : null;
            r && r.handleError(e)
        }
        function gm(n, e, t, r, i) {
            for (let o = 0; o < t.length; ) {
                const s = t[o++]
                  , a = t[o++]
                  , l = e[s]
                  , u = n.data[s];
                null !== u.setInput ? u.setInput(l, i, r, a) : l[a] = i
            }
        }
        function An(n, e, t) {
            const r = rs(e, n);
            !function vp(n, e, t) {
                Ce(n) ? n.setValue(e, t) : e.textContent = t
            }(n[$], r, t)
        }
        function Rs(n, e, t) {
            let r = t ? n.styles : null
              , i = t ? n.classes : null
              , o = 0;
            if (null !== e)
                for (let s = 0; s < e.length; s++) {
                    const a = e[s];
                    "number" == typeof a ? o = a : 1 == o ? i = vl(i, a) : 2 == o && (r = vl(r, a + ": " + e[++s] + ";"))
                }
            t ? n.styles = r : n.stylesWithoutHost = r,
            t ? n.classes = i : n.classesWithoutHost = i
        }
        const Ku = new S("INJECTOR",-1);
        class ym {
            get(e, t=Gi) {
                if (t === Gi) {
                    const r = new Error(`NullInjectorError: No provider for ${te(e)}!`);
                    throw r.name = "NullInjectorError",
                    r
                }
                return t
            }
        }
        const Qu = new S("Set Injector scope.")
          , ro = {}
          , SM = {};
        let Zu;
        function _m() {
            return void 0 === Zu && (Zu = new ym),
            Zu
        }
        function vm(n, e=null, t=null, r) {
            const i = bm(n, e, t, r);
            return i._resolveInjectorDefTypes(),
            i
        }
        function bm(n, e=null, t=null, r) {
            return new xM(n,t,e || _m(),r)
        }
        class xM {
            constructor(e, t, r, i=null) {
                this.parent = r,
                this.records = new Map,
                this.injectorDefTypes = new Set,
                this.onDestroy = new Set,
                this._destroyed = !1;
                const o = [];
                t && ln(t, a=>this.processProvider(a, e, t)),
                ln([e], a=>this.processInjectorType(a, [], o)),
                this.records.set(Ku, ei(void 0, this));
                const s = this.records.get(Qu);
                this.scope = null != s ? s.value : null,
                this.source = i || ("object" == typeof e ? null : te(e))
            }
            get destroyed() {
                return this._destroyed
            }
            destroy() {
                this.assertNotDestroyed(),
                this._destroyed = !0;
                try {
                    this.onDestroy.forEach(e=>e.ngOnDestroy())
                } finally {
                    this.records.clear(),
                    this.onDestroy.clear(),
                    this.injectorDefTypes.clear()
                }
            }
            get(e, t=Gi, r=H.Default) {
                this.assertNotDestroyed();
                const i = $h(this)
                  , o = Rn(void 0);
                try {
                    if (!(r & H.SkipSelf)) {
                        let a = this.records.get(e);
                        if (void 0 === a) {
                            const l = function VM(n) {
                                return "function" == typeof n || "object" == typeof n && n instanceof S
                            }(e) && Dl(e);
                            a = l && this.injectableDefInScope(l) ? ei(Yu(e), ro) : null,
                            this.records.set(e, a)
                        }
                        if (null != a)
                            return this.hydrate(e, a)
                    }
                    return (r & H.Self ? _m() : this.parent).get(e, t = r & H.Optional && t === Gi ? null : t)
                } catch (s) {
                    if ("NullInjectorError" === s.name) {
                        if ((s[bs] = s[bs] || []).unshift(te(e)),
                        i)
                            throw s;
                        return function aw(n, e, t, r) {
                            const i = n[bs];
                            throw e[Uh] && i.unshift(e[Uh]),
                            n.message = function lw(n, e, t, r=null) {
                                n = n && "\n" === n.charAt(0) && "\u0275" == n.charAt(1) ? n.substr(2) : n;
                                let i = te(e);
                                if (Array.isArray(e))
                                    i = e.map(te).join(" -> ");
                                else if ("object" == typeof e) {
                                    let o = [];
                                    for (let s in e)
                                        if (e.hasOwnProperty(s)) {
                                            let a = e[s];
                                            o.push(s + ":" + ("string" == typeof a ? JSON.stringify(a) : te(a)))
                                        }
                                    i = `{${o.join(", ")}}`
                                }
                                return `${t}${r ? "(" + r + ")" : ""}[${i}]: ${n.replace(nw, "\n  ")}`
                            }("\n" + n.message, i, t, r),
                            n.ngTokenPath = i,
                            n[bs] = null,
                            n
                        }(s, e, "R3InjectorError", this.source)
                    }
                    throw s
                } finally {
                    Rn(o),
                    $h(i)
                }
            }
            _resolveInjectorDefTypes() {
                this.injectorDefTypes.forEach(e=>this.get(e))
            }
            toString() {
                const e = [];
                return this.records.forEach((r,i)=>e.push(te(i))),
                `R3Injector[${e.join(", ")}]`
            }
            assertNotDestroyed() {
                if (this._destroyed)
                    throw new M(205,!1)
            }
            processInjectorType(e, t, r) {
                if (!(e = U(e)))
                    return !1;
                let i = Jf(e);
                const o = null == i && e.ngModule || void 0
                  , s = void 0 === o ? e : o
                  , a = -1 !== r.indexOf(s);
                if (void 0 !== o && (i = Jf(o)),
                null == i)
                    return !1;
                if (null != i.imports && !a) {
                    let c;
                    r.push(s);
                    try {
                        ln(i.imports, d=>{
                            this.processInjectorType(d, t, r) && (void 0 === c && (c = []),
                            c.push(d))
                        }
                        )
                    } finally {}
                    if (void 0 !== c)
                        for (let d = 0; d < c.length; d++) {
                            const {ngModule: f, providers: h} = c[d];
                            ln(h, p=>this.processProvider(p, f, h || ie))
                        }
                }
                this.injectorDefTypes.add(s);
                const l = lr(s) || (()=>new s);
                this.records.set(s, ei(l, ro));
                const u = i.providers;
                if (null != u && !a) {
                    const c = e;
                    ln(u, d=>this.processProvider(d, c, u))
                }
                return void 0 !== o && void 0 !== e.providers
            }
            processProvider(e, t, r) {
                let i = ti(e = U(e)) ? e : U(e && e.provide);
                const o = function NM(n, e, t) {
                    return Cm(n) ? ei(void 0, n.useValue) : ei(Dm(n), ro)
                }(e);
                if (ti(e) || !0 !== e.multi)
                    this.records.get(i);
                else {
                    let s = this.records.get(i);
                    s || (s = ei(void 0, ro, !0),
                    s.factory = ()=>nu(s.multi),
                    this.records.set(i, s)),
                    i = e,
                    s.multi.push(e)
                }
                this.records.set(i, o)
            }
            hydrate(e, t) {
                return t.value === ro && (t.value = SM,
                t.value = t.factory()),
                "object" == typeof t.value && t.value && function LM(n) {
                    return null !== n && "object" == typeof n && "function" == typeof n.ngOnDestroy
                }(t.value) && this.onDestroy.add(t.value),
                t.value
            }
            injectableDefInScope(e) {
                if (!e.providedIn)
                    return !1;
                const t = U(e.providedIn);
                return "string" == typeof t ? "any" === t || t === this.scope : this.injectorDefTypes.has(t)
            }
        }
        function Yu(n) {
            const e = Dl(n)
              , t = null !== e ? e.factory : lr(n);
            if (null !== t)
                return t;
            if (n instanceof S)
                throw new M(204,!1);
            if (n instanceof Function)
                return function FM(n) {
                    const e = n.length;
                    if (e > 0)
                        throw $i(e, "?"),
                        new M(204,!1);
                    const t = function HC(n) {
                        const e = n && (n[Zo] || n[eh]);
                        if (e) {
                            const t = function UC(n) {
                                if (n.hasOwnProperty("name"))
                                    return n.name;
                                const e = ("" + n).match(/^function\s*([^\s(]+)/);
                                return null === e ? "" : e[1]
                            }(n);
                            return console.warn(`DEPRECATED: DI is instantiating a token "${t}" that inherits its @Injectable decorator but does not provide one itself.\nThis will become an error in a future version of Angular. Please add @Injectable() to the "${t}" class.`),
                            e
                        }
                        return null
                    }(n);
                    return null !== t ? ()=>t.factory(n) : ()=>new n
                }(n);
            throw new M(204,!1)
        }
        function Dm(n, e, t) {
            let r;
            if (ti(n)) {
                const i = U(n);
                return lr(i) || Yu(i)
            }
            if (Cm(n))
                r = ()=>U(n.useValue);
            else if (function kM(n) {
                return !(!n || !n.useFactory)
            }(n))
                r = ()=>n.useFactory(...nu(n.deps || []));
            else if (function OM(n) {
                return !(!n || !n.useExisting)
            }(n))
                r = ()=>w(U(n.useExisting));
            else {
                const i = U(n && (n.useClass || n.provide));
                if (!function PM(n) {
                    return !!n.deps
                }(n))
                    return lr(i) || Yu(i);
                r = ()=>new i(...nu(n.deps))
            }
            return r
        }
        function ei(n, e, t=!1) {
            return {
                factory: n,
                value: e,
                multi: t ? [] : void 0
            }
        }
        function Cm(n) {
            return null !== n && "object" == typeof n && iw in n
        }
        function ti(n) {
            return "function" == typeof n
        }
        let vt = (()=>{
            class n {
                static create(t, r) {
                    var i;
                    if (Array.isArray(t))
                        return vm({
                            name: ""
                        }, r, t, "");
                    {
                        const o = null !== (i = t.name) && void 0 !== i ? i : "";
                        return vm({
                            name: o
                        }, t.parent, t.providers, o)
                    }
                }
            }
            return n.THROW_IF_NOT_FOUND = Gi,
            n.NULL = new ym,
            n.\u0275prov = R({
                token: n,
                providedIn: "any",
                factory: ()=>w(Ku)
            }),
            n.__NG_ELEMENT_ID__ = -1,
            n
        }
        )();
        function qM(n, e) {
            ls(fu(n)[1], Ne())
        }
        function Y(n) {
            let e = function km(n) {
                return Object.getPrototypeOf(n.prototype).constructor
            }(n.type)
              , t = !0;
            const r = [n];
            for (; e; ) {
                let i;
                if (Wt(n))
                    i = e.\u0275cmp || e.\u0275dir;
                else {
                    if (e.\u0275cmp)
                        throw new M(903,"");
                    i = e.\u0275dir
                }
                if (i) {
                    if (t) {
                        r.push(i);
                        const s = n;
                        s.inputs = ec(n.inputs),
                        s.declaredInputs = ec(n.declaredInputs),
                        s.outputs = ec(n.outputs);
                        const a = i.hostBindings;
                        a && ZM(n, a);
                        const l = i.viewQuery
                          , u = i.contentQueries;
                        if (l && KM(n, l),
                        u && QM(n, u),
                        _l(n.inputs, i.inputs),
                        _l(n.declaredInputs, i.declaredInputs),
                        _l(n.outputs, i.outputs),
                        Wt(i) && i.data.animation) {
                            const c = n.data;
                            c.animation = (c.animation || []).concat(i.data.animation)
                        }
                    }
                    const o = i.features;
                    if (o)
                        for (let s = 0; s < o.length; s++) {
                            const a = o[s];
                            a && a.ngInherit && a(n),
                            a === Y && (t = !1)
                        }
                }
                e = Object.getPrototypeOf(e)
            }
            !function WM(n) {
                let e = 0
                  , t = null;
                for (let r = n.length - 1; r >= 0; r--) {
                    const i = n[r];
                    i.hostVars = e += i.hostVars,
                    i.hostAttrs = fs(i.hostAttrs, t = fs(t, i.hostAttrs))
                }
            }(r)
        }
        function ec(n) {
            return n === Nr ? {} : n === ie ? [] : n
        }
        function KM(n, e) {
            const t = n.viewQuery;
            n.viewQuery = t ? (r,i)=>{
                e(r, i),
                t(r, i)
            }
            : e
        }
        function QM(n, e) {
            const t = n.contentQueries;
            n.contentQueries = t ? (r,i,o)=>{
                e(r, i, o),
                t(r, i, o)
            }
            : e
        }
        function ZM(n, e) {
            const t = n.hostBindings;
            n.hostBindings = t ? (r,i)=>{
                e(r, i),
                t(r, i)
            }
            : e
        }
        let Ps = null;
        function ni() {
            if (!Ps) {
                const n = ne.Symbol;
                if (n && n.iterator)
                    Ps = n.iterator;
                else {
                    const e = Object.getOwnPropertyNames(Map.prototype);
                    for (let t = 0; t < e.length; ++t) {
                        const r = e[t];
                        "entries" !== r && "size" !== r && Map.prototype[r] === Map.prototype.entries && (Ps = r)
                    }
                }
            }
            return Ps
        }
        function io(n) {
            return !!function tc(n) {
                return null !== n && ("function" == typeof n || "object" == typeof n)
            }(n) && (Array.isArray(n) || !(n instanceof Map) && ni()in n)
        }
        function We(n, e, t) {
            return !Object.is(n[e], t) && (n[e] = t,
            !0)
        }
        function bt(n, e, t, r) {
            const i = b();
            return We(i, Vr(), e) && (Q(),
            fn(Ee(), i, n, e, t, r)),
            bt
        }
        function ut(n, e, t, r, i, o, s, a) {
            const l = b()
              , u = Q()
              , c = n + 20
              , d = u.firstCreatePass ? function rA(n, e, t, r, i, o, s, a, l) {
                const u = e.consts
                  , c = Yr(e, n, 4, s || null, Vn(u, a));
                Hu(e, t, c, Vn(u, l)),
                ls(e, c);
                const d = c.tViews = Os(2, c, r, i, o, e.directiveRegistry, e.pipeRegistry, null, e.schemas, u);
                return null !== e.queries && (e.queries.template(e, c),
                d.queries = e.queries.embeddedTView(c)),
                c
            }(c, u, l, e, t, r, i, o, s) : u.data[c];
            an(d, !1);
            const f = l[$].createComment("");
            Is(u, l, f, d),
            qe(f, l),
            ks(l, l[c] = cm(f, l, f, d)),
            ns(d) && Bu(u, l, d),
            null != s && ju(l, d, a)
        }
        function v(n, e=H.Default) {
            const t = b();
            return null === t ? w(n, e) : Nh(Ne(), t, U(n), e)
        }
        function fe(n, e, t) {
            const r = b();
            return We(r, Vr(), e) && _t(Q(), Ee(), r, n, e, r[$], t, !1),
            fe
        }
        function sc(n, e, t, r, i) {
            const s = i ? "class" : "style";
            gm(n, t, e.inputs[s], s, r)
        }
        function B(n, e, t, r) {
            const i = b()
              , o = Q()
              , s = 20 + n
              , a = i[$]
              , l = i[s] = bu(a, e, function NE() {
                return P.lFrame.currentNamespace
            }())
              , u = o.firstCreatePass ? function AA(n, e, t, r, i, o, s) {
                const a = e.consts
                  , u = Yr(e, n, 2, i, Vn(a, o));
                return Hu(e, t, u, Vn(a, s)),
                null !== u.attrs && Rs(u, u.attrs, !1),
                null !== u.mergedAttrs && Rs(u, u.mergedAttrs, !0),
                null !== e.queries && e.queries.elementStart(e, u),
                u
            }(s, o, i, 0, e, t, r) : o.data[s];
            an(u, !0);
            const c = u.mergedAttrs;
            null !== c && ds(a, l, c);
            const d = u.classes;
            null !== d && Au(a, l, d);
            const f = u.styles;
            return null !== f && Op(a, l, f),
            64 != (64 & u.flags) && Is(o, i, l, u),
            0 === function gE() {
                return P.lFrame.elementDepthCount
            }() && qe(l, i),
            function yE() {
                P.lFrame.elementDepthCount++
            }(),
            ns(u) && (Bu(o, i, u),
            Xp(o, u, i)),
            null !== r && ju(i, u),
            B
        }
        function j() {
            let n = Ne();
            Bl() ? jl() : (n = n.parent,
            an(n, !1));
            const e = n;
            !function _E() {
                P.lFrame.elementDepthCount--
            }();
            const t = Q();
            return t.firstCreatePass && (ls(t, n),
            Il(n) && t.queries.elementEnd(n)),
            null != e.classesWithoutHost && function LE(n) {
                return 0 != (16 & n.flags)
            }(e) && sc(t, e, b(), e.classesWithoutHost, !0),
            null != e.stylesWithoutHost && function VE(n) {
                return 0 != (32 & n.flags)
            }(e) && sc(t, e, b(), e.stylesWithoutHost, !1),
            j
        }
        function ke(n, e, t, r) {
            return B(n, e, t, r),
            j(),
            ke
        }
        function so(n, e, t) {
            const r = b()
              , i = Q()
              , o = n + 20
              , s = i.firstCreatePass ? function TA(n, e, t, r, i) {
                const o = e.consts
                  , s = Vn(o, r)
                  , a = Yr(e, n, 8, "ng-container", s);
                return null !== s && Rs(a, s, !0),
                Hu(e, t, a, Vn(o, i)),
                null !== e.queries && e.queries.elementStart(e, a),
                a
            }(o, i, r, e, t) : i.data[o];
            an(s, !0);
            const a = r[o] = r[$].createComment("");
            return Is(i, r, a, s),
            qe(a, r),
            ns(s) && (Bu(i, r, s),
            Xp(i, s, r)),
            null != t && ju(r, s),
            so
        }
        function ao() {
            let n = Ne();
            const e = Q();
            return Bl() ? jl() : (n = n.parent,
            an(n, !1)),
            e.firstCreatePass && (ls(e, n),
            Il(n) && e.queries.elementEnd(n)),
            ao
        }
        function ac() {
            return b()
        }
        function Bs(n) {
            return !!n && "function" == typeof n.then
        }
        const ng = function tg(n) {
            return !!n && "function" == typeof n.subscribe
        };
        function Ke(n, e, t, r) {
            const i = b()
              , o = Q()
              , s = Ne();
            return function ig(n, e, t, r, i, o, s, a) {
                const l = ns(r)
                  , c = n.firstCreatePass && hm(n)
                  , d = e[8]
                  , f = fm(e);
                let h = !0;
                if (3 & r.type || a) {
                    const y = Rt(r, e)
                      , _ = a ? a(y) : y
                      , g = f.length
                      , D = a ? I=>a(Te(I[r.index])) : r.index;
                    if (Ce(t)) {
                        let I = null;
                        if (!a && l && (I = function IA(n, e, t, r) {
                            const i = n.cleanup;
                            if (null != i)
                                for (let o = 0; o < i.length - 1; o += 2) {
                                    const s = i[o];
                                    if (s === t && i[o + 1] === r) {
                                        const a = e[7]
                                          , l = i[o + 2];
                                        return a.length > l ? a[l] : null
                                    }
                                    "string" == typeof s && (o += 2)
                                }
                            return null
                        }(n, e, i, r.index)),
                        null !== I)
                            (I.__ngLastListenerFn__ || I).__ngNextListenerFn__ = o,
                            I.__ngLastListenerFn__ = o,
                            h = !1;
                        else {
                            o = lc(r, e, d, o, !1);
                            const z = t.listen(_, i, o);
                            f.push(o, z),
                            c && c.push(i, D, g, g + 1)
                        }
                    } else
                        o = lc(r, e, d, o, !0),
                        _.addEventListener(i, o, s),
                        f.push(o),
                        c && c.push(i, D, g, s)
                } else
                    o = lc(r, e, d, o, !1);
                const p = r.outputs;
                let m;
                if (h && null !== p && (m = p[i])) {
                    const y = m.length;
                    if (y)
                        for (let _ = 0; _ < y; _ += 2) {
                            const ye = e[m[_]][m[_ + 1]].subscribe(o)
                              , be = f.length;
                            f.push(o, ye),
                            c && c.push(i, r.index, be, -(be + 1))
                        }
                }
            }(o, i, i[$], s, n, e, !!t, r),
            Ke
        }
        function og(n, e, t, r) {
            try {
                return !1 !== t(r)
            } catch (i) {
                return mm(n, i),
                !1
            }
        }
        function lc(n, e, t, r, i) {
            return function o(s) {
                if (s === Function)
                    return r;
                const a = 2 & n.flags ? pt(n.index, e) : e;
                0 == (32 & e[2]) && Gu(a);
                let l = og(e, 0, r, s)
                  , u = o.__ngNextListenerFn__;
                for (; u; )
                    l = og(e, 0, u, s) && l,
                    u = u.__ngNextListenerFn__;
                return i && !1 === l && (s.preventDefault(),
                s.returnValue = !1),
                l
            }
        }
        function pn(n=1) {
            return function AE(n) {
                return (P.lFrame.contextLView = function TE(n, e) {
                    for (; n > 0; )
                        e = e[15],
                        n--;
                    return e
                }(n, P.lFrame.contextLView))[8]
            }(n)
        }
        function SA(n, e) {
            let t = null;
            const r = function R0(n) {
                const e = n.attrs;
                if (null != e) {
                    const t = e.indexOf(5);
                    if (0 == (1 & t))
                        return e[t + 1]
                }
                return null
            }(n);
            for (let i = 0; i < e.length; i++) {
                const o = e[i];
                if ("*" !== o) {
                    if (null === r ? Lp(n, o, !0) : V0(r, o))
                        return i
                } else
                    t = i
            }
            return t
        }
        function hr(n) {
            const e = b()[16][6];
            if (!e.projection) {
                const r = e.projection = $i(n ? n.length : 1, null)
                  , i = r.slice();
                let o = e.child;
                for (; null !== o; ) {
                    const s = n ? SA(o, n) : 0;
                    null !== s && (i[s] ? i[s].projectionNext = o : r[s] = o,
                    i[s] = o),
                    o = o.next
                }
            }
        }
        function Be(n, e=0, t) {
            const r = b()
              , i = Q()
              , o = Yr(i, 20 + n, 16, null, t || null);
            null === o.projection && (o.projection = e),
            jl(),
            64 != (64 & o.flags) && function I0(n, e, t) {
                Np(e[$], 0, e, t, Cp(n, t, e), Ap(t.parent || e[6], t, e))
            }(i, r, o)
        }
        function mg(n, e, t, r, i) {
            const o = n[t + 1]
              , s = null === e;
            let a = r ? Qt(o) : Mn(o)
              , l = !1;
            for (; 0 !== a && (!1 === l || s); ) {
                const c = n[a + 1];
                NA(n[a], e) && (l = !0,
                n[a + 1] = r ? Su(c) : Tu(c)),
                a = r ? Qt(c) : Mn(c)
            }
            l && (n[t + 1] = r ? Tu(o) : Su(o))
        }
        function NA(n, e) {
            return null === n || null == e || (Array.isArray(n) ? n[1] : n) === e || !(!Array.isArray(n) || "string" != typeof e) && qr(n, e) >= 0
        }
        function Je(n, e) {
            return function Yt(n, e, t, r) {
                const i = b()
                  , o = Q()
                  , s = function wn(n) {
                    const e = P.lFrame
                      , t = e.bindingIndex;
                    return e.bindingIndex = e.bindingIndex + n,
                    t
                }(2);
                o.firstUpdatePass && function wg(n, e, t, r) {
                    const i = n.data;
                    if (null === i[t + 1]) {
                        const o = i[Ye()]
                          , s = function Eg(n, e) {
                            return e >= n.expandoStartIndex
                        }(n, t);
                        (function Ig(n, e) {
                            return 0 != (n.flags & (e ? 16 : 32))
                        }
                        )(o, r) && null === e && !s && (e = !1),
                        e = function HA(n, e, t, r) {
                            const i = function Ul(n) {
                                const e = P.lFrame.currentDirectiveIndex;
                                return -1 === e ? null : n[e]
                            }(n);
                            let o = r ? e.residualClasses : e.residualStyles;
                            if (null === i)
                                0 === (r ? e.classBindings : e.styleBindings) && (t = lo(t = cc(null, n, e, t, r), e.attrs, r),
                                o = null);
                            else {
                                const s = e.directiveStylingLast;
                                if (-1 === s || n[s] !== i)
                                    if (t = cc(i, n, e, t, r),
                                    null === o) {
                                        let l = function UA(n, e, t) {
                                            const r = t ? e.classBindings : e.styleBindings;
                                            if (0 !== Mn(r))
                                                return n[Qt(r)]
                                        }(n, e, r);
                                        void 0 !== l && Array.isArray(l) && (l = cc(null, n, e, l[1], r),
                                        l = lo(l, e.attrs, r),
                                        function $A(n, e, t, r) {
                                            n[Qt(t ? e.classBindings : e.styleBindings)] = r
                                        }(n, e, r, l))
                                    } else
                                        o = function GA(n, e, t) {
                                            let r;
                                            const i = e.directiveEnd;
                                            for (let o = 1 + e.directiveStylingLast; o < i; o++)
                                                r = lo(r, n[o].hostAttrs, t);
                                            return lo(r, e.attrs, t)
                                        }(n, e, r)
                            }
                            return void 0 !== o && (r ? e.residualClasses = o : e.residualStyles = o),
                            t
                        }(i, o, e, r),
                        function xA(n, e, t, r, i, o) {
                            let s = o ? e.classBindings : e.styleBindings
                              , a = Qt(s)
                              , l = Mn(s);
                            n[r] = t;
                            let c, u = !1;
                            if (Array.isArray(t)) {
                                const d = t;
                                c = d[1],
                                (null === c || qr(d, c) > 0) && (u = !0)
                            } else
                                c = t;
                            if (i)
                                if (0 !== l) {
                                    const f = Qt(n[a + 1]);
                                    n[r + 1] = xs(f, a),
                                    0 !== f && (n[f + 1] = Iu(n[f + 1], r)),
                                    n[a + 1] = function U0(n, e) {
                                        return 131071 & n | e << 17
                                    }(n[a + 1], r)
                                } else
                                    n[r + 1] = xs(a, 0),
                                    0 !== a && (n[a + 1] = Iu(n[a + 1], r)),
                                    a = r;
                            else
                                n[r + 1] = xs(l, 0),
                                0 === a ? a = r : n[l + 1] = Iu(n[l + 1], r),
                                l = r;
                            u && (n[r + 1] = Tu(n[r + 1])),
                            mg(n, c, r, !0),
                            mg(n, c, r, !1),
                            function FA(n, e, t, r, i) {
                                const o = i ? n.residualClasses : n.residualStyles;
                                null != o && "string" == typeof e && qr(o, e) >= 0 && (t[r + 1] = Su(t[r + 1]))
                            }(e, c, n, r, o),
                            s = xs(a, l),
                            o ? e.classBindings = s : e.styleBindings = s
                        }(i, o, e, t, s, r)
                    }
                }(o, n, s, r),
                e !== V && We(i, s, e) && function Ag(n, e, t, r, i, o, s, a) {
                    if (!(3 & e.type))
                        return;
                    const l = n.data
                      , u = l[a + 1];
                    js(function Up(n) {
                        return 1 == (1 & n)
                    }(u) ? Tg(l, e, t, i, Mn(u), s) : void 0) || (js(o) || function Hp(n) {
                        return 2 == (2 & n)
                    }(u) && (o = Tg(l, null, t, i, a, s)),
                    function x0(n, e, t, r, i) {
                        const o = Ce(n);
                        if (e)
                            i ? o ? n.addClass(t, r) : t.classList.add(r) : o ? n.removeClass(t, r) : t.classList.remove(r);
                        else {
                            let s = -1 === r.indexOf("-") ? void 0 : yt.DashCase;
                            if (null == i)
                                o ? n.removeStyle(t, r, s) : t.style.removeProperty(r);
                            else {
                                const a = "string" == typeof i && i.endsWith("!important");
                                a && (i = i.slice(0, -10),
                                s |= yt.Important),
                                o ? n.setStyle(t, r, i, s) : t.style.setProperty(r, i, a ? "important" : "")
                            }
                        }
                    }(r, s, rs(Ye(), t), i, o))
                }(o, o.data[Ye()], i, i[$], n, i[s + 1] = function WA(n, e) {
                    return null == n || ("string" == typeof e ? n += e : "object" == typeof n && (n = te(gt(n)))),
                    n
                }(e, t), r, s)
            }(n, e, null, !0),
            Je
        }
        function cc(n, e, t, r, i) {
            let o = null;
            const s = t.directiveEnd;
            let a = t.directiveStylingLast;
            for (-1 === a ? a = t.directiveStart : a++; a < s && (o = e[a],
            r = lo(r, o.hostAttrs, i),
            o !== n); )
                a++;
            return null !== n && (t.directiveStylingLast = a),
            r
        }
        function lo(n, e, t) {
            const r = t ? 1 : 2;
            let i = -1;
            if (null !== e)
                for (let o = 0; o < e.length; o++) {
                    const s = e[o];
                    "number" == typeof s ? i = s : i === r && (Array.isArray(n) || (n = void 0 === n ? [] : ["", n]),
                    mt(n, s, !!t || e[++o]))
                }
            return void 0 === n ? null : n
        }
        function Tg(n, e, t, r, i, o) {
            const s = null === e;
            let a;
            for (; i > 0; ) {
                const l = n[i]
                  , u = Array.isArray(l)
                  , c = u ? l[1] : l
                  , d = null === c;
                let f = t[i + 1];
                f === V && (f = d ? ie : void 0);
                let h = d ? Jl(f, r) : c === r ? f : void 0;
                if (u && !js(h) && (h = Jl(l, r)),
                js(h) && (a = h,
                s))
                    return a;
                const p = n[i + 1];
                i = s ? Qt(p) : Mn(p)
            }
            if (null !== e) {
                let l = o ? e.residualClasses : e.residualStyles;
                null != l && (a = Jl(l, r))
            }
            return a
        }
        function js(n) {
            return void 0 !== n
        }
        function me(n, e="") {
            const t = b()
              , r = Q()
              , i = n + 20
              , o = r.firstCreatePass ? Yr(r, i, 1, e, null) : r.data[i]
              , s = t[i] = function vu(n, e) {
                return Ce(n) ? n.createText(e) : n.createTextNode(e)
            }(t[$], e);
            Is(r, t, s, o),
            an(o, !1)
        }
        function pr(n) {
            return dc("", n, ""),
            pr
        }
        function dc(n, e, t) {
            const r = b()
              , i = function ii(n, e, t, r) {
                return We(n, Vr(), t) ? e + L(t) + r : V
            }(r, n, e, t);
            return i !== V && An(r, Ye(), i),
            dc
        }
        function fc(n, e, t) {
            const r = b();
            return We(r, Vr(), e) && _t(Q(), Ee(), r, n, e, r[$], t, !0),
            fc
        }
        const Hs = "en-US";
        let Qg = Hs;
        function mc(n, e, t, r, i) {
            if (n = U(n),
            Array.isArray(n))
                for (let o = 0; o < n.length; o++)
                    mc(n[o], e, t, r, i);
            else {
                const o = Q()
                  , s = b();
                let a = ti(n) ? n : U(n.provide)
                  , l = Dm(n);
                const u = Ne()
                  , c = 1048575 & u.providerIndexes
                  , d = u.directiveStart
                  , f = u.providerIndexes >> 20;
                if (ti(n) || !n.multi) {
                    const h = new Li(l,i,v)
                      , p = yc(a, e, i ? c : c + f, d);
                    -1 === p ? (ms(Bi(u, s), o, a),
                    gc(o, n, e.length),
                    e.push(a),
                    u.directiveStart++,
                    u.directiveEnd++,
                    i && (u.providerIndexes += 1048576),
                    t.push(h),
                    s.push(h)) : (t[p] = h,
                    s[p] = h)
                } else {
                    const h = yc(a, e, c + f, d)
                      , p = yc(a, e, c, c + f)
                      , m = h >= 0 && t[h]
                      , y = p >= 0 && t[p];
                    if (i && !y || !i && !m) {
                        ms(Bi(u, s), o, a);
                        const _ = function fI(n, e, t, r, i) {
                            const o = new Li(n,t,v);
                            return o.multi = [],
                            o.index = e,
                            o.componentProviders = 0,
                            vy(o, i, r && !t),
                            o
                        }(i ? dI : cI, t.length, i, r, l);
                        !i && y && (t[p].providerFactory = _),
                        gc(o, n, e.length, 0),
                        e.push(a),
                        u.directiveStart++,
                        u.directiveEnd++,
                        i && (u.providerIndexes += 1048576),
                        t.push(_),
                        s.push(_)
                    } else
                        gc(o, n, h > -1 ? h : p, vy(t[i ? p : h], l, !i && r));
                    !i && r && y && t[p].componentProviders++
                }
            }
        }
        function gc(n, e, t, r) {
            const i = ti(e)
              , o = function RM(n) {
                return !!n.useClass
            }(e);
            if (i || o) {
                const l = (o ? U(e.useClass) : e).prototype.ngOnDestroy;
                if (l) {
                    const u = n.destroyHooks || (n.destroyHooks = []);
                    if (!i && e.multi) {
                        const c = u.indexOf(t);
                        -1 === c ? u.push(t, [r, l]) : u[c + 1].push(r, l)
                    } else
                        u.push(t, l)
                }
            }
        }
        function vy(n, e, t) {
            return t && n.componentProviders++,
            n.multi.push(e) - 1
        }
        function yc(n, e, t, r) {
            for (let i = t; i < r; i++)
                if (e[i] === n)
                    return i;
            return -1
        }
        function cI(n, e, t, r) {
            return _c(this.multi, [])
        }
        function dI(n, e, t, r) {
            const i = this.multi;
            let o;
            if (this.providerFactory) {
                const s = this.providerFactory.componentProviders
                  , a = ji(t, t[1], this.providerFactory.index, r);
                o = a.slice(0, s),
                _c(i, o);
                for (let l = s; l < a.length; l++)
                    o.push(a[l])
            } else
                o = [],
                _c(i, o);
            return o
        }
        function _c(n, e) {
            for (let t = 0; t < n.length; t++)
                e.push((0,
                n[t])());
            return e
        }
        function ae(n, e=[]) {
            return t=>{
                t.providersResolver = (r,i)=>function uI(n, e, t) {
                    const r = Q();
                    if (r.firstCreatePass) {
                        const i = Wt(n);
                        mc(t, r.data, r.blueprint, i, !0),
                        mc(e, r.data, r.blueprint, i, !1)
                    }
                }(r, i ? i(n) : n, e)
            }
        }
        class by {
        }
        class mI {
            resolveComponentFactory(e) {
                throw function pI(n) {
                    const e = Error(`No component factory found for ${te(n)}. Did you add it to @NgModule.entryComponents?`);
                    return e.ngComponent = n,
                    e
                }(e)
            }
        }
        let qs = (()=>{
            class n {
            }
            return n.NULL = new mI,
            n
        }
        )();
        function gI() {
            return gi(Ne(), b())
        }
        function gi(n, e) {
            return new Pe(Rt(n, e))
        }
        let Pe = (()=>{
            class n {
                constructor(t) {
                    this.nativeElement = t
                }
            }
            return n.__NG_ELEMENT_ID__ = gI,
            n
        }
        )();
        function yI(n) {
            return n instanceof Pe ? n.nativeElement : n
        }
        class po {
        }
        let gr = (()=>{
            class n {
            }
            return n.__NG_ELEMENT_ID__ = ()=>function vI() {
                const n = b()
                  , t = pt(Ne().index, n);
                return function _I(n) {
                    return n[$]
                }(on(t) ? t : n)
            }(),
            n
        }
        )()
          , bI = (()=>{
            class n {
            }
            return n.\u0275prov = R({
                token: n,
                providedIn: "root",
                factory: ()=>null
            }),
            n
        }
        )();
        class yi {
            constructor(e) {
                this.full = e,
                this.major = e.split(".")[0],
                this.minor = e.split(".")[1],
                this.patch = e.split(".").slice(2).join(".")
            }
        }
        const DI = new yi("13.3.4")
          , vc = {};
        function Ws(n, e, t, r, i=!1) {
            for (; null !== t; ) {
                const o = e[t.index];
                if (null !== o && r.push(Te(o)),
                qt(o))
                    for (let a = 10; a < o.length; a++) {
                        const l = o[a]
                          , u = l[1].firstChild;
                        null !== u && Ws(l[1], l, u, r)
                    }
                const s = t.type;
                if (8 & s)
                    Ws(n, e, t.child, r);
                else if (32 & s) {
                    const a = gu(t, e);
                    let l;
                    for (; l = a(); )
                        r.push(l)
                } else if (16 & s) {
                    const a = xp(e, t);
                    if (Array.isArray(a))
                        r.push(...a);
                    else {
                        const l = Ji(e[16]);
                        Ws(l[1], l, a, r, !0)
                    }
                }
                t = i ? t.projectionNext : t.next
            }
            return r
        }
        class mo {
            constructor(e, t) {
                this._lView = e,
                this._cdRefInjectingView = t,
                this._appRef = null,
                this._attachedToViewContainer = !1
            }
            get rootNodes() {
                const e = this._lView
                  , t = e[1];
                return Ws(t, e, t.firstChild, [])
            }
            get context() {
                return this._lView[8]
            }
            set context(e) {
                this._lView[8] = e
            }
            get destroyed() {
                return 256 == (256 & this._lView[2])
            }
            destroy() {
                if (this._appRef)
                    this._appRef.detachView(this);
                else if (this._attachedToViewContainer) {
                    const e = this._lView[3];
                    if (qt(e)) {
                        const t = e[8]
                          , r = t ? t.indexOf(this) : -1;
                        r > -1 && (Du(e, r),
                        _s(t, r))
                    }
                    this._attachedToViewContainer = !1
                }
                Dp(this._lView[1], this._lView)
            }
            onDestroy(e) {
                nm(this._lView[1], this._lView, null, e)
            }
            markForCheck() {
                Gu(this._cdRefInjectingView || this._lView)
            }
            detach() {
                this._lView[2] &= -129
            }
            reattach() {
                this._lView[2] |= 128
            }
            detectChanges() {
                qu(this._lView[1], this._lView, this.context)
            }
            checkNoChanges() {
                !function wM(n, e, t) {
                    os(!0);
                    try {
                        qu(n, e, t)
                    } finally {
                        os(!1)
                    }
                }(this._lView[1], this._lView, this.context)
            }
            attachToViewContainerRef() {
                if (this._appRef)
                    throw new M(902,"");
                this._attachedToViewContainer = !0
            }
            detachFromAppRef() {
                this._appRef = null,
                function b0(n, e) {
                    eo(n, e, e[$], 2, null, null)
                }(this._lView[1], this._lView)
            }
            attachToAppRef(e) {
                if (this._attachedToViewContainer)
                    throw new M(902,"");
                this._appRef = e
            }
        }
        class CI extends mo {
            constructor(e) {
                super(e),
                this._view = e
            }
            detectChanges() {
                dm(this._view)
            }
            checkNoChanges() {
                !function MM(n) {
                    os(!0);
                    try {
                        dm(n)
                    } finally {
                        os(!1)
                    }
                }(this._view)
            }
            get context() {
                return null
            }
        }
        class Cy extends qs {
            constructor(e) {
                super(),
                this.ngModule = e
            }
            resolveComponentFactory(e) {
                const t = $e(e);
                return new bc(t,this.ngModule)
            }
        }
        function Ey(n) {
            const e = [];
            for (let t in n)
                n.hasOwnProperty(t) && e.push({
                    propName: n[t],
                    templateName: t
                });
            return e
        }
        class bc extends by {
            constructor(e, t) {
                super(),
                this.componentDef = e,
                this.ngModule = t,
                this.componentType = e.type,
                this.selector = function j0(n) {
                    return n.map(B0).join(",")
                }(e.selectors),
                this.ngContentSelectors = e.ngContentSelectors ? e.ngContentSelectors : [],
                this.isBoundToModule = !!t
            }
            get inputs() {
                return Ey(this.componentDef.inputs)
            }
            get outputs() {
                return Ey(this.componentDef.outputs)
            }
            create(e, t, r, i) {
                const o = (i = i || this.ngModule) ? function wI(n, e) {
                    return {
                        get: (t,r,i)=>{
                            const o = n.get(t, vc, i);
                            return o !== vc || r === vc ? o : e.get(t, r, i)
                        }
                    }
                }(e, i.injector) : e
                  , s = o.get(po, dh)
                  , a = o.get(bI, null)
                  , l = s.createRenderer(null, this.componentDef)
                  , u = this.componentDef.selectors[0][0] || "div"
                  , c = r ? function tm(n, e, t) {
                    if (Ce(n))
                        return n.selectRootElement(e, t === Gt.ShadowDom);
                    let r = "string" == typeof e ? n.querySelector(e) : e;
                    return r.textContent = "",
                    r
                }(l, r, this.componentDef.encapsulation) : bu(s.createRenderer(null, this.componentDef), u, function EI(n) {
                    const e = n.toLowerCase();
                    return "svg" === e ? "svg" : "math" === e ? "math" : null
                }(u))
                  , d = this.componentDef.onPush ? 576 : 528
                  , f = function Om(n, e) {
                    return {
                        components: [],
                        scheduler: n || f0,
                        clean: AM,
                        playerHandler: e || null,
                        flags: 0
                    }
                }()
                  , h = Os(0, null, null, 1, 0, null, null, null, null, null)
                  , p = to(null, h, f, d, null, null, s, l, a, o);
                let m, y;
                ss(p);
                try {
                    const _ = function Fm(n, e, t, r, i, o) {
                        const s = t[1];
                        t[20] = n;
                        const l = Yr(s, 20, 2, "#host", null)
                          , u = l.mergedAttrs = e.hostAttrs;
                        null !== u && (Rs(l, u, !0),
                        null !== n && (ds(i, n, u),
                        null !== l.classes && Au(i, n, l.classes),
                        null !== l.styles && Op(i, n, l.styles)));
                        const c = r.createRenderer(n, e)
                          , d = to(t, Jp(e), null, e.onPush ? 64 : 16, t[20], l, r, c, o || null, null);
                        return s.firstCreatePass && (ms(Bi(l, t), s, e.type),
                        am(s, l),
                        lm(l, t.length, 1)),
                        ks(t, d),
                        t[20] = d
                    }(c, this.componentDef, p, s, l);
                    if (c)
                        if (r)
                            ds(l, c, ["ng-version", DI.full]);
                        else {
                            const {attrs: g, classes: D} = function H0(n) {
                                const e = []
                                  , t = [];
                                let r = 1
                                  , i = 2;
                                for (; r < n.length; ) {
                                    let o = n[r];
                                    if ("string" == typeof o)
                                        2 === i ? "" !== o && e.push(o, n[++r]) : 8 === i && t.push(o);
                                    else {
                                        if (!Kt(i))
                                            break;
                                        i = o
                                    }
                                    r++
                                }
                                return {
                                    attrs: e,
                                    classes: t
                                }
                            }(this.componentDef.selectors[0]);
                            g && ds(l, c, g),
                            D && D.length > 0 && Au(l, c, D.join(" "))
                        }
                    if (y = Rl(h, 20),
                    void 0 !== t) {
                        const g = y.projection = [];
                        for (let D = 0; D < this.ngContentSelectors.length; D++) {
                            const I = t[D];
                            g.push(null != I ? Array.from(I) : null)
                        }
                    }
                    m = function Nm(n, e, t, r, i) {
                        const o = t[1]
                          , s = function lM(n, e, t) {
                            const r = Ne();
                            n.firstCreatePass && (t.providersResolver && t.providersResolver(t),
                            um(n, r, e, Xr(n, e, 1, null), t));
                            const i = ji(e, n, r.directiveStart, r);
                            qe(i, e);
                            const o = Rt(r, e);
                            return o && qe(o, e),
                            i
                        }(o, t, e);
                        if (r.components.push(s),
                        n[8] = s,
                        i && i.forEach(l=>l(s, e)),
                        e.contentQueries) {
                            const l = Ne();
                            e.contentQueries(1, s, l.directiveStart)
                        }
                        const a = Ne();
                        return !o.firstCreatePass || null === e.hostBindings && null === e.hostAttrs || (Bn(a.index),
                        om(t[1], a, 0, a.directiveStart, a.directiveEnd, e),
                        sm(e, s)),
                        s
                    }(_, this.componentDef, p, f, [qM]),
                    no(h, p, null)
                } finally {
                    as()
                }
                return new AI(this.componentType,m,gi(y, p),p,y)
            }
        }
        class AI extends class hI {
        }
        {
            constructor(e, t, r, i, o) {
                super(),
                this.location = r,
                this._rootLView = i,
                this._tNode = o,
                this.instance = t,
                this.hostView = this.changeDetectorRef = new CI(i),
                this.componentType = e
            }
            get injector() {
                return new Hr(this._tNode,this._rootLView)
            }
            destroy() {
                this.hostView.destroy()
            }
            onDestroy(e) {
                this.hostView.onDestroy(e)
            }
        }
        class _i {
        }
        const vi = new Map;
        class Ay extends _i {
            constructor(e, t) {
                super(),
                this._parent = t,
                this._bootstrapComponents = [],
                this.injector = this,
                this.destroyCbs = [],
                this.componentFactoryResolver = new Cy(this);
                const r = Nt(e);
                this._bootstrapComponents = dn(r.bootstrap),
                this._r3Injector = bm(e, t, [{
                    provide: _i,
                    useValue: this
                }, {
                    provide: qs,
                    useValue: this.componentFactoryResolver
                }], te(e)),
                this._r3Injector._resolveInjectorDefTypes(),
                this.instance = this.get(e)
            }
            get(e, t=vt.THROW_IF_NOT_FOUND, r=H.Default) {
                return e === vt || e === _i || e === Ku ? this : this._r3Injector.get(e, t, r)
            }
            destroy() {
                const e = this._r3Injector;
                !e.destroyed && e.destroy(),
                this.destroyCbs.forEach(t=>t()),
                this.destroyCbs = null
            }
            onDestroy(e) {
                this.destroyCbs.push(e)
            }
        }
        class Dc extends class II {
        }
        {
            constructor(e) {
                super(),
                this.moduleType = e,
                null !== Nt(e) && function SI(n) {
                    const e = new Set;
                    !function t(r) {
                        const i = Nt(r, !0)
                          , o = i.id;
                        null !== o && (function wy(n, e, t) {
                            if (e && e !== t)
                                throw new Error(`Duplicate module registered for ${n} - ${te(e)} vs ${te(e.name)}`)
                        }(o, vi.get(o), r),
                        vi.set(o, r));
                        const s = dn(i.imports);
                        for (const a of s)
                            e.has(a) || (e.add(a),
                            t(a))
                    }(n)
                }(e)
            }
            create(e) {
                return new Ay(this.moduleType,e)
            }
        }
        function Cc(n) {
            return e=>{
                setTimeout(n, void 0, e)
            }
        }
        const je = class WI extends Ut {
            constructor(e=!1) {
                super(),
                this.__isAsync = e
            }
            emit(e) {
                super.next(e)
            }
            subscribe(e, t, r) {
                var i, o, s;
                let a = e
                  , l = t || (()=>null)
                  , u = r;
                if (e && "object" == typeof e) {
                    const d = e;
                    a = null === (i = d.next) || void 0 === i ? void 0 : i.bind(d),
                    l = null === (o = d.error) || void 0 === o ? void 0 : o.bind(d),
                    u = null === (s = d.complete) || void 0 === s ? void 0 : s.bind(d)
                }
                this.__isAsync && (l = Cc(l),
                a && (a = Cc(a)),
                u && (u = Cc(u)));
                const c = super.subscribe({
                    next: a,
                    error: l,
                    complete: u
                });
                return e instanceof It && e.add(c),
                c
            }
        }
        ;
        function KI() {
            return this._results[ni()]()
        }
        class Ec {
            constructor(e=!1) {
                this._emitDistinctChangesOnly = e,
                this.dirty = !0,
                this._results = [],
                this._changesDetected = !1,
                this._changes = null,
                this.length = 0,
                this.first = void 0,
                this.last = void 0;
                const t = ni()
                  , r = Ec.prototype;
                r[t] || (r[t] = KI)
            }
            get changes() {
                return this._changes || (this._changes = new je)
            }
            get(e) {
                return this._results[e]
            }
            map(e) {
                return this._results.map(e)
            }
            filter(e) {
                return this._results.filter(e)
            }
            find(e) {
                return this._results.find(e)
            }
            reduce(e, t) {
                return this._results.reduce(e, t)
            }
            forEach(e) {
                this._results.forEach(e)
            }
            some(e) {
                return this._results.some(e)
            }
            toArray() {
                return this._results.slice()
            }
            toString() {
                return this._results.toString()
            }
            reset(e, t) {
                const r = this;
                r.dirty = !1;
                const i = Pt(e);
                (this._changesDetected = !function WE(n, e, t) {
                    if (n.length !== e.length)
                        return !1;
                    for (let r = 0; r < n.length; r++) {
                        let i = n[r]
                          , o = e[r];
                        if (t && (i = t(i),
                        o = t(o)),
                        o !== i)
                            return !1
                    }
                    return !0
                }(r._results, i, t)) && (r._results = i,
                r.length = i.length,
                r.last = i[this.length - 1],
                r.first = i[0])
            }
            notifyOnChanges() {
                this._changes && (this._changesDetected || !this._emitDistinctChangesOnly) && this._changes.emit(this)
            }
            setDirty() {
                this.dirty = !0
            }
            destroy() {
                this.changes.complete(),
                this.changes.unsubscribe()
            }
        }
        Symbol;
        let Tn = (()=>{
            class n {
            }
            return n.__NG_ELEMENT_ID__ = YI,
            n
        }
        )();
        const QI = Tn
          , ZI = class extends QI {
            constructor(e, t, r) {
                super(),
                this._declarationLView = e,
                this._declarationTContainer = t,
                this.elementRef = r
            }
            createEmbeddedView(e) {
                const t = this._declarationTContainer.tViews
                  , r = to(this._declarationLView, t, e, 16, null, t.declTNode, null, null, null, null);
                r[17] = this._declarationLView[this._declarationTContainer.index];
                const o = this._declarationLView[19];
                return null !== o && (r[19] = o.createEmbeddedView(t)),
                no(t, r, e),
                new mo(r)
            }
        }
        ;
        function YI() {
            return Ks(Ne(), b())
        }
        function Ks(n, e) {
            return 4 & n.type ? new ZI(e,n,gi(n, e)) : null
        }
        let yn = (()=>{
            class n {
            }
            return n.__NG_ELEMENT_ID__ = XI,
            n
        }
        )();
        function XI() {
            return ky(Ne(), b())
        }
        const JI = yn
          , Ny = class extends JI {
            constructor(e, t, r) {
                super(),
                this._lContainer = e,
                this._hostTNode = t,
                this._hostLView = r
            }
            get element() {
                return gi(this._hostTNode, this._hostLView)
            }
            get injector() {
                return new Hr(this._hostTNode,this._hostLView)
            }
            get parentInjector() {
                const e = ps(this._hostTNode, this._hostLView);
                if (Th(e)) {
                    const t = jr(e, this._hostLView)
                      , r = Br(e);
                    return new Hr(t[1].data[r + 8],t)
                }
                return new Hr(null,this._hostLView)
            }
            clear() {
                for (; this.length > 0; )
                    this.remove(this.length - 1)
            }
            get(e) {
                const t = Oy(this._lContainer);
                return null !== t && t[e] || null
            }
            get length() {
                return this._lContainer.length - 10
            }
            createEmbeddedView(e, t, r) {
                const i = e.createEmbeddedView(t || {});
                return this.insert(i, r),
                i
            }
            createComponent(e, t, r, i, o) {
                const s = e && !function Ui(n) {
                    return "function" == typeof n
                }(e);
                let a;
                if (s)
                    a = t;
                else {
                    const d = t || {};
                    a = d.index,
                    r = d.injector,
                    i = d.projectableNodes,
                    o = d.ngModuleRef
                }
                const l = s ? e : new bc($e(e))
                  , u = r || this.parentInjector;
                if (!o && null == l.ngModule) {
                    const f = (s ? u : this.parentInjector).get(_i, null);
                    f && (o = f)
                }
                const c = l.create(u, i, void 0, o);
                return this.insert(c.hostView, a),
                c
            }
            insert(e, t) {
                const r = e._lView
                  , i = r[1];
                if (function mE(n) {
                    return qt(n[3])
                }(r)) {
                    const c = this.indexOf(e);
                    if (-1 !== c)
                        this.detach(c);
                    else {
                        const d = r[3]
                          , f = new Ny(d,d[6],d[3]);
                        f.detach(f.indexOf(e))
                    }
                }
                const o = this._adjustIndex(t)
                  , s = this._lContainer;
                !function C0(n, e, t, r) {
                    const i = 10 + r
                      , o = t.length;
                    r > 0 && (t[i - 1][4] = e),
                    r < o - 10 ? (e[4] = t[i],
                    Lh(t, 10 + r, e)) : (t.push(e),
                    e[4] = null),
                    e[3] = t;
                    const s = e[17];
                    null !== s && t !== s && function E0(n, e) {
                        const t = n[9];
                        e[16] !== e[3][3][16] && (n[2] = !0),
                        null === t ? n[9] = [e] : t.push(e)
                    }(s, e);
                    const a = e[19];
                    null !== a && a.insertView(n),
                    e[2] |= 128
                }(i, r, s, o);
                const a = wu(o, s)
                  , l = r[$]
                  , u = Ts(l, s[7]);
                return null !== u && function v0(n, e, t, r, i, o) {
                    r[0] = i,
                    r[6] = e,
                    eo(n, r, t, 1, i, o)
                }(i, s[6], l, r, u, a),
                e.attachToViewContainerRef(),
                Lh(wc(s), o, e),
                e
            }
            move(e, t) {
                return this.insert(e, t)
            }
            indexOf(e) {
                const t = Oy(this._lContainer);
                return null !== t ? t.indexOf(e) : -1
            }
            remove(e) {
                const t = this._adjustIndex(e, -1)
                  , r = Du(this._lContainer, t);
                r && (_s(wc(this._lContainer), t),
                Dp(r[1], r))
            }
            detach(e) {
                const t = this._adjustIndex(e, -1)
                  , r = Du(this._lContainer, t);
                return r && null != _s(wc(this._lContainer), t) ? new mo(r) : null
            }
            _adjustIndex(e, t=0) {
                return null == e ? this.length + t : e
            }
        }
        ;
        function Oy(n) {
            return n[8]
        }
        function wc(n) {
            return n[8] || (n[8] = [])
        }
        function ky(n, e) {
            let t;
            const r = e[n.index];
            if (qt(r))
                t = r;
            else {
                let i;
                if (8 & n.type)
                    i = Te(r);
                else {
                    const o = e[$];
                    i = o.createComment("");
                    const s = Rt(n, e);
                    dr(o, Ts(o, s), i, function T0(n, e) {
                        return Ce(n) ? n.nextSibling(e) : e.nextSibling
                    }(o, s), !1)
                }
                e[n.index] = t = cm(r, e, i, n),
                ks(e, t)
            }
            return new Ny(t,n,e)
        }
        class Mc {
            constructor(e) {
                this.queryList = e,
                this.matches = null
            }
            clone() {
                return new Mc(this.queryList)
            }
            setDirty() {
                this.queryList.setDirty()
            }
        }
        class Ac {
            constructor(e=[]) {
                this.queries = e
            }
            createEmbeddedView(e) {
                const t = e.queries;
                if (null !== t) {
                    const r = null !== e.contentQueries ? e.contentQueries[0] : t.length
                      , i = [];
                    for (let o = 0; o < r; o++) {
                        const s = t.getByIndex(o);
                        i.push(this.queries[s.indexInDeclarationView].clone())
                    }
                    return new Ac(i)
                }
                return null
            }
            insertView(e) {
                this.dirtyQueriesWithMatches(e)
            }
            detachView(e) {
                this.dirtyQueriesWithMatches(e)
            }
            dirtyQueriesWithMatches(e) {
                for (let t = 0; t < this.queries.length; t++)
                    null !== By(e, t).matches && this.queries[t].setDirty()
            }
        }
        class Ry {
            constructor(e, t, r=null) {
                this.predicate = e,
                this.flags = t,
                this.read = r
            }
        }
        class Tc {
            constructor(e=[]) {
                this.queries = e
            }
            elementStart(e, t) {
                for (let r = 0; r < this.queries.length; r++)
                    this.queries[r].elementStart(e, t)
            }
            elementEnd(e) {
                for (let t = 0; t < this.queries.length; t++)
                    this.queries[t].elementEnd(e)
            }
            embeddedTView(e) {
                let t = null;
                for (let r = 0; r < this.length; r++) {
                    const i = null !== t ? t.length : 0
                      , o = this.getByIndex(r).embeddedTView(e, i);
                    o && (o.indexInDeclarationView = r,
                    null !== t ? t.push(o) : t = [o])
                }
                return null !== t ? new Tc(t) : null
            }
            template(e, t) {
                for (let r = 0; r < this.queries.length; r++)
                    this.queries[r].template(e, t)
            }
            getByIndex(e) {
                return this.queries[e]
            }
            get length() {
                return this.queries.length
            }
            track(e) {
                this.queries.push(e)
            }
        }
        class Ic {
            constructor(e, t=-1) {
                this.metadata = e,
                this.matches = null,
                this.indexInDeclarationView = -1,
                this.crossesNgTemplate = !1,
                this._appliesToNextNode = !0,
                this._declarationNodeIndex = t
            }
            elementStart(e, t) {
                this.isApplyingToNode(t) && this.matchTNode(e, t)
            }
            elementEnd(e) {
                this._declarationNodeIndex === e.index && (this._appliesToNextNode = !1)
            }
            template(e, t) {
                this.elementStart(e, t)
            }
            embeddedTView(e, t) {
                return this.isApplyingToNode(e) ? (this.crossesNgTemplate = !0,
                this.addMatch(-e.index, t),
                new Ic(this.metadata)) : null
            }
            isApplyingToNode(e) {
                if (this._appliesToNextNode && 1 != (1 & this.metadata.flags)) {
                    const t = this._declarationNodeIndex;
                    let r = e.parent;
                    for (; null !== r && 8 & r.type && r.index !== t; )
                        r = r.parent;
                    return t === (null !== r ? r.index : -1)
                }
                return this._appliesToNextNode
            }
            matchTNode(e, t) {
                const r = this.metadata.predicate;
                if (Array.isArray(r))
                    for (let i = 0; i < r.length; i++) {
                        const o = r[i];
                        this.matchTNodeWithReadOption(e, t, nS(t, o)),
                        this.matchTNodeWithReadOption(e, t, gs(t, e, o, !1, !1))
                    }
                else
                    r === Tn ? 4 & t.type && this.matchTNodeWithReadOption(e, t, -1) : this.matchTNodeWithReadOption(e, t, gs(t, e, r, !1, !1))
            }
            matchTNodeWithReadOption(e, t, r) {
                if (null !== r) {
                    const i = this.metadata.read;
                    if (null !== i)
                        if (i === Pe || i === yn || i === Tn && 4 & t.type)
                            this.addMatch(t.index, -2);
                        else {
                            const o = gs(t, e, i, !1, !1);
                            null !== o && this.addMatch(t.index, o)
                        }
                    else
                        this.addMatch(t.index, r)
                }
            }
            addMatch(e, t) {
                null === this.matches ? this.matches = [e, t] : this.matches.push(e, t)
            }
        }
        function nS(n, e) {
            const t = n.localNames;
            if (null !== t)
                for (let r = 0; r < t.length; r += 2)
                    if (t[r] === e)
                        return t[r + 1];
            return null
        }
        function iS(n, e, t, r) {
            return -1 === t ? function rS(n, e) {
                return 11 & n.type ? gi(n, e) : 4 & n.type ? Ks(n, e) : null
            }(e, n) : -2 === t ? function oS(n, e, t) {
                return t === Pe ? gi(e, n) : t === Tn ? Ks(e, n) : t === yn ? ky(e, n) : void 0
            }(n, e, r) : ji(n, n[1], t, e)
        }
        function Py(n, e, t, r) {
            const i = e[19].queries[r];
            if (null === i.matches) {
                const o = n.data
                  , s = t.matches
                  , a = [];
                for (let l = 0; l < s.length; l += 2) {
                    const u = s[l];
                    a.push(u < 0 ? null : iS(e, o[u], s[l + 1], t.metadata.read))
                }
                i.matches = a
            }
            return i.matches
        }
        function Sc(n, e, t, r) {
            const i = n.queries.getByIndex(t)
              , o = i.matches;
            if (null !== o) {
                const s = Py(n, e, i, t);
                for (let a = 0; a < o.length; a += 2) {
                    const l = o[a];
                    if (l > 0)
                        r.push(s[a / 2]);
                    else {
                        const u = o[a + 1]
                          , c = e[-l];
                        for (let d = 10; d < c.length; d++) {
                            const f = c[d];
                            f[17] === f[3] && Sc(f[1], f, u, r)
                        }
                        if (null !== c[9]) {
                            const d = c[9];
                            for (let f = 0; f < d.length; f++) {
                                const h = d[f];
                                Sc(h[1], h, u, r)
                            }
                        }
                    }
                }
            }
            return r
        }
        function tt(n) {
            const e = b()
              , t = Q()
              , r = _h();
            $l(r + 1);
            const i = By(t, r);
            if (n.dirty && fh(e) === (2 == (2 & i.metadata.flags))) {
                if (null === i.matches)
                    n.reset([]);
                else {
                    const o = i.crossesNgTemplate ? Sc(t, e, r, []) : Py(t, e, i, r);
                    n.reset(o, yI),
                    n.notifyOnChanges()
                }
                return !0
            }
            return !1
        }
        function _o(n, e, t) {
            const r = Q();
            r.firstCreatePass && (Vy(r, new Ry(n,e,t), -1),
            2 == (2 & e) && (r.staticViewQueries = !0)),
            Ly(r, b(), e)
        }
        function Jt(n, e, t, r) {
            const i = Q();
            if (i.firstCreatePass) {
                const o = Ne();
                Vy(i, new Ry(e,t,r), o.index),
                function aS(n, e) {
                    const t = n.contentQueries || (n.contentQueries = []);
                    e !== (t.length ? t[t.length - 1] : -1) && t.push(n.queries.length - 1, e)
                }(i, n),
                2 == (2 & t) && (i.staticContentQueries = !0)
            }
            Ly(i, b(), t)
        }
        function nt() {
            return function sS(n, e) {
                return n[19].queries[e].queryList
            }(b(), _h())
        }
        function Ly(n, e, t) {
            const r = new Ec(4 == (4 & t));
            nm(n, e, r, r.destroy),
            null === e[19] && (e[19] = new Ac),
            e[19].queries.push(new Mc(r))
        }
        function Vy(n, e, t) {
            null === n.queries && (n.queries = new Tc),
            n.queries.track(new Ic(e,t))
        }
        function By(n, e) {
            return n.queries.getByIndex(e)
        }
        function Ys(...n) {}
        const n_ = new S("Application Initializer");
        let Rc = (()=>{
            class n {
                constructor(t) {
                    this.appInits = t,
                    this.resolve = Ys,
                    this.reject = Ys,
                    this.initialized = !1,
                    this.done = !1,
                    this.donePromise = new Promise((r,i)=>{
                        this.resolve = r,
                        this.reject = i
                    }
                    )
                }
                runInitializers() {
                    if (this.initialized)
                        return;
                    const t = []
                      , r = ()=>{
                        this.done = !0,
                        this.resolve()
                    }
                    ;
                    if (this.appInits)
                        for (let i = 0; i < this.appInits.length; i++) {
                            const o = this.appInits[i]();
                            if (Bs(o))
                                t.push(o);
                            else if (ng(o)) {
                                const s = new Promise((a,l)=>{
                                    o.subscribe({
                                        complete: a,
                                        error: l
                                    })
                                }
                                );
                                t.push(s)
                            }
                        }
                    Promise.all(t).then(()=>{
                        r()
                    }
                    ).catch(i=>{
                        this.reject(i)
                    }
                    ),
                    0 === t.length && r(),
                    this.initialized = !0
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(n_, 8))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        const bo = new S("AppId",{
            providedIn: "root",
            factory: function r_() {
                return `${Pc()}${Pc()}${Pc()}`
            }
        });
        function Pc() {
            return String.fromCharCode(97 + Math.floor(25 * Math.random()))
        }
        const i_ = new S("Platform Initializer")
          , Xs = new S("Platform ID",{
            providedIn: "platform",
            factory: ()=>"unknown"
        })
          , MS = new S("appBootstrapListener")
          , In = new S("LocaleId",{
            providedIn: "root",
            factory: ()=>Ds(In, H.Optional | H.SkipSelf) || function AS() {
                return "undefined" != typeof $localize && $localize.locale || Hs
            }()
        })
          , xS = (()=>Promise.resolve(0))();
        function Lc(n) {
            "undefined" == typeof Zone ? xS.then(()=>{
                n && n.apply(null, null)
            }
            ) : Zone.current.scheduleMicroTask("scheduleMicrotask", n)
        }
        class _e {
            constructor({enableLongStackTrace: e=!1, shouldCoalesceEventChangeDetection: t=!1, shouldCoalesceRunChangeDetection: r=!1}) {
                if (this.hasPendingMacrotasks = !1,
                this.hasPendingMicrotasks = !1,
                this.isStable = !0,
                this.onUnstable = new je(!1),
                this.onMicrotaskEmpty = new je(!1),
                this.onStable = new je(!1),
                this.onError = new je(!1),
                "undefined" == typeof Zone)
                    throw new Error("In this configuration Angular requires Zone.js");
                Zone.assertZonePatched();
                const i = this;
                i._nesting = 0,
                i._outer = i._inner = Zone.current,
                Zone.TaskTrackingZoneSpec && (i._inner = i._inner.fork(new Zone.TaskTrackingZoneSpec)),
                e && Zone.longStackTraceZoneSpec && (i._inner = i._inner.fork(Zone.longStackTraceZoneSpec)),
                i.shouldCoalesceEventChangeDetection = !r && t,
                i.shouldCoalesceRunChangeDetection = r,
                i.lastRequestAnimationFrameId = -1,
                i.nativeRequestAnimationFrame = function FS() {
                    let n = ne.requestAnimationFrame
                      , e = ne.cancelAnimationFrame;
                    if ("undefined" != typeof Zone && n && e) {
                        const t = n[Zone.__symbol__("OriginalDelegate")];
                        t && (n = t);
                        const r = e[Zone.__symbol__("OriginalDelegate")];
                        r && (e = r)
                    }
                    return {
                        nativeRequestAnimationFrame: n,
                        nativeCancelAnimationFrame: e
                    }
                }().nativeRequestAnimationFrame,
                function kS(n) {
                    const e = ()=>{
                        !function OS(n) {
                            n.isCheckStableRunning || -1 !== n.lastRequestAnimationFrameId || (n.lastRequestAnimationFrameId = n.nativeRequestAnimationFrame.call(ne, ()=>{
                                n.fakeTopEventTask || (n.fakeTopEventTask = Zone.root.scheduleEventTask("fakeTopEventTask", ()=>{
                                    n.lastRequestAnimationFrameId = -1,
                                    Bc(n),
                                    n.isCheckStableRunning = !0,
                                    Vc(n),
                                    n.isCheckStableRunning = !1
                                }
                                , void 0, ()=>{}
                                , ()=>{}
                                )),
                                n.fakeTopEventTask.invoke()
                            }
                            ),
                            Bc(n))
                        }(n)
                    }
                    ;
                    n._inner = n._inner.fork({
                        name: "angular",
                        properties: {
                            isAngularZone: !0
                        },
                        onInvokeTask: (t,r,i,o,s,a)=>{
                            try {
                                return o_(n),
                                t.invokeTask(i, o, s, a)
                            } finally {
                                (n.shouldCoalesceEventChangeDetection && "eventTask" === o.type || n.shouldCoalesceRunChangeDetection) && e(),
                                s_(n)
                            }
                        }
                        ,
                        onInvoke: (t,r,i,o,s,a,l)=>{
                            try {
                                return o_(n),
                                t.invoke(i, o, s, a, l)
                            } finally {
                                n.shouldCoalesceRunChangeDetection && e(),
                                s_(n)
                            }
                        }
                        ,
                        onHasTask: (t,r,i,o)=>{
                            t.hasTask(i, o),
                            r === i && ("microTask" == o.change ? (n._hasPendingMicrotasks = o.microTask,
                            Bc(n),
                            Vc(n)) : "macroTask" == o.change && (n.hasPendingMacrotasks = o.macroTask))
                        }
                        ,
                        onHandleError: (t,r,i,o)=>(t.handleError(i, o),
                        n.runOutsideAngular(()=>n.onError.emit(o)),
                        !1)
                    })
                }(i)
            }
            static isInAngularZone() {
                return "undefined" != typeof Zone && !0 === Zone.current.get("isAngularZone")
            }
            static assertInAngularZone() {
                if (!_e.isInAngularZone())
                    throw new Error("Expected to be in Angular Zone, but it is not!")
            }
            static assertNotInAngularZone() {
                if (_e.isInAngularZone())
                    throw new Error("Expected to not be in Angular Zone, but it is!")
            }
            run(e, t, r) {
                return this._inner.run(e, t, r)
            }
            runTask(e, t, r, i) {
                const o = this._inner
                  , s = o.scheduleEventTask("NgZoneEvent: " + i, e, NS, Ys, Ys);
                try {
                    return o.runTask(s, t, r)
                } finally {
                    o.cancelTask(s)
                }
            }
            runGuarded(e, t, r) {
                return this._inner.runGuarded(e, t, r)
            }
            runOutsideAngular(e) {
                return this._outer.run(e)
            }
        }
        const NS = {};
        function Vc(n) {
            if (0 == n._nesting && !n.hasPendingMicrotasks && !n.isStable)
                try {
                    n._nesting++,
                    n.onMicrotaskEmpty.emit(null)
                } finally {
                    if (n._nesting--,
                    !n.hasPendingMicrotasks)
                        try {
                            n.runOutsideAngular(()=>n.onStable.emit(null))
                        } finally {
                            n.isStable = !0
                        }
                }
        }
        function Bc(n) {
            n.hasPendingMicrotasks = !!(n._hasPendingMicrotasks || (n.shouldCoalesceEventChangeDetection || n.shouldCoalesceRunChangeDetection) && -1 !== n.lastRequestAnimationFrameId)
        }
        function o_(n) {
            n._nesting++,
            n.isStable && (n.isStable = !1,
            n.onUnstable.emit(null))
        }
        function s_(n) {
            n._nesting--,
            Vc(n)
        }
        class RS {
            constructor() {
                this.hasPendingMicrotasks = !1,
                this.hasPendingMacrotasks = !1,
                this.isStable = !0,
                this.onUnstable = new je,
                this.onMicrotaskEmpty = new je,
                this.onStable = new je,
                this.onError = new je
            }
            run(e, t, r) {
                return e.apply(t, r)
            }
            runGuarded(e, t, r) {
                return e.apply(t, r)
            }
            runOutsideAngular(e) {
                return e()
            }
            runTask(e, t, r, i) {
                return e.apply(t, r)
            }
        }
        let jc = (()=>{
            class n {
                constructor(t) {
                    this._ngZone = t,
                    this._pendingCount = 0,
                    this._isZoneStable = !0,
                    this._didWork = !1,
                    this._callbacks = [],
                    this.taskTrackingZone = null,
                    this._watchAngularEvents(),
                    t.run(()=>{
                        this.taskTrackingZone = "undefined" == typeof Zone ? null : Zone.current.get("TaskTrackingZone")
                    }
                    )
                }
                _watchAngularEvents() {
                    this._ngZone.onUnstable.subscribe({
                        next: ()=>{
                            this._didWork = !0,
                            this._isZoneStable = !1
                        }
                    }),
                    this._ngZone.runOutsideAngular(()=>{
                        this._ngZone.onStable.subscribe({
                            next: ()=>{
                                _e.assertNotInAngularZone(),
                                Lc(()=>{
                                    this._isZoneStable = !0,
                                    this._runCallbacksIfReady()
                                }
                                )
                            }
                        })
                    }
                    )
                }
                increasePendingRequestCount() {
                    return this._pendingCount += 1,
                    this._didWork = !0,
                    this._pendingCount
                }
                decreasePendingRequestCount() {
                    if (this._pendingCount -= 1,
                    this._pendingCount < 0)
                        throw new Error("pending async requests below zero");
                    return this._runCallbacksIfReady(),
                    this._pendingCount
                }
                isStable() {
                    return this._isZoneStable && 0 === this._pendingCount && !this._ngZone.hasPendingMacrotasks
                }
                _runCallbacksIfReady() {
                    if (this.isStable())
                        Lc(()=>{
                            for (; 0 !== this._callbacks.length; ) {
                                let t = this._callbacks.pop();
                                clearTimeout(t.timeoutId),
                                t.doneCb(this._didWork)
                            }
                            this._didWork = !1
                        }
                        );
                    else {
                        let t = this.getPendingTasks();
                        this._callbacks = this._callbacks.filter(r=>!r.updateCb || !r.updateCb(t) || (clearTimeout(r.timeoutId),
                        !1)),
                        this._didWork = !0
                    }
                }
                getPendingTasks() {
                    return this.taskTrackingZone ? this.taskTrackingZone.macroTasks.map(t=>({
                        source: t.source,
                        creationLocation: t.creationLocation,
                        data: t.data
                    })) : []
                }
                addCallback(t, r, i) {
                    let o = -1;
                    r && r > 0 && (o = setTimeout(()=>{
                        this._callbacks = this._callbacks.filter(s=>s.timeoutId !== o),
                        t(this._didWork, this.getPendingTasks())
                    }
                    , r)),
                    this._callbacks.push({
                        doneCb: t,
                        timeoutId: o,
                        updateCb: i
                    })
                }
                whenStable(t, r, i) {
                    if (i && !this.taskTrackingZone)
                        throw new Error('Task tracking zone is required when passing an update callback to whenStable(). Is "zone.js/plugins/task-tracking" loaded?');
                    this.addCallback(t, r, i),
                    this._runCallbacksIfReady()
                }
                getPendingRequestCount() {
                    return this._pendingCount
                }
                findProviders(t, r, i) {
                    return []
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(_e))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )()
          , PS = (()=>{
            class n {
                constructor() {
                    this._applications = new Map,
                    Hc.addToWindow(this)
                }
                registerApplication(t, r) {
                    this._applications.set(t, r)
                }
                unregisterApplication(t) {
                    this._applications.delete(t)
                }
                unregisterAllApplications() {
                    this._applications.clear()
                }
                getTestability(t) {
                    return this._applications.get(t) || null
                }
                getAllTestabilities() {
                    return Array.from(this._applications.values())
                }
                getAllRootElements() {
                    return Array.from(this._applications.keys())
                }
                findTestabilityInTree(t, r=!0) {
                    return Hc.findTestabilityInTree(this, t, r)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "platform"
            }),
            n
        }
        )();
        class LS {
            addToWindow(e) {}
            findTestabilityInTree(e, t, r) {
                return null
            }
        }
        let Hc = new LS
          , yr = null;
        const a_ = new S("AllowMultipleToken")
          , l_ = new S("PlatformOnDestroy");
        function u_(n, e, t=[]) {
            const r = `Platform: ${e}`
              , i = new S(r);
            return (o=[])=>{
                let s = Uc();
                if (!s || s.injector.get(a_, !1)) {
                    const a = [...t, ...o, {
                        provide: i,
                        useValue: !0
                    }];
                    n ? n(a) : function HS(n) {
                        if (yr && !yr.get(a_, !1))
                            throw new M(400,"");
                        yr = n;
                        const e = n.get(c_)
                          , t = n.get(i_, null);
                        t && t.forEach(r=>r())
                    }(function $S(n=[], e) {
                        return vt.create({
                            name: e,
                            providers: [{
                                provide: Qu,
                                useValue: "platform"
                            }, {
                                provide: l_,
                                useValue: ()=>yr = null
                            }, ...n]
                        })
                    }(a, r))
                }
                return function US(n) {
                    const e = Uc();
                    if (!e)
                        throw new M(401,"");
                    return e
                }()
            }
        }
        function Uc() {
            var n;
            return null !== (n = null == yr ? void 0 : yr.get(c_)) && void 0 !== n ? n : null
        }
        let c_ = (()=>{
            class n {
                constructor(t) {
                    this._injector = t,
                    this._modules = [],
                    this._destroyListeners = [],
                    this._destroyed = !1
                }
                bootstrapModuleFactory(t, r) {
                    const a = function GS(n, e) {
                        let t;
                        return t = "noop" === n ? new RS : ("zone.js" === n ? void 0 : n) || new _e({
                            enableLongStackTrace: !1,
                            shouldCoalesceEventChangeDetection: !!(null == e ? void 0 : e.ngZoneEventCoalescing),
                            shouldCoalesceRunChangeDetection: !!(null == e ? void 0 : e.ngZoneRunCoalescing)
                        }),
                        t
                    }(r ? r.ngZone : void 0, {
                        ngZoneEventCoalescing: r && r.ngZoneEventCoalescing || !1,
                        ngZoneRunCoalescing: r && r.ngZoneRunCoalescing || !1
                    })
                      , l = [{
                        provide: _e,
                        useValue: a
                    }];
                    return a.run(()=>{
                        const u = vt.create({
                            providers: l,
                            parent: this.injector,
                            name: t.moduleType.name
                        })
                          , c = t.create(u)
                          , d = c.injector.get(Hn, null);
                        if (!d)
                            throw new M(402,"");
                        return a.runOutsideAngular(()=>{
                            const f = a.onError.subscribe({
                                next: h=>{
                                    d.handleError(h)
                                }
                            });
                            c.onDestroy(()=>{
                                $c(this._modules, c),
                                f.unsubscribe()
                            }
                            )
                        }
                        ),
                        function zS(n, e, t) {
                            try {
                                const r = t();
                                return Bs(r) ? r.catch(i=>{
                                    throw e.runOutsideAngular(()=>n.handleError(i)),
                                    i
                                }
                                ) : r
                            } catch (r) {
                                throw e.runOutsideAngular(()=>n.handleError(r)),
                                r
                            }
                        }(d, a, ()=>{
                            const f = c.injector.get(Rc);
                            return f.runInitializers(),
                            f.donePromise.then(()=>(function _T(n) {
                                ft(n, "Expected localeId to be defined"),
                                "string" == typeof n && (Qg = n.toLowerCase().replace(/_/g, "-"))
                            }(c.injector.get(In, Hs) || Hs),
                            this._moduleDoBootstrap(c),
                            c))
                        }
                        )
                    }
                    )
                }
                bootstrapModule(t, r=[]) {
                    const i = d_({}, r);
                    return function BS(n, e, t) {
                        const r = new Dc(t);
                        return Promise.resolve(r)
                    }(0, 0, t).then(o=>this.bootstrapModuleFactory(o, i))
                }
                _moduleDoBootstrap(t) {
                    const r = t.injector.get(f_);
                    if (t._bootstrapComponents.length > 0)
                        t._bootstrapComponents.forEach(i=>r.bootstrap(i));
                    else {
                        if (!t.instance.ngDoBootstrap)
                            throw new M(403,"");
                        t.instance.ngDoBootstrap(r)
                    }
                    this._modules.push(t)
                }
                onDestroy(t) {
                    this._destroyListeners.push(t)
                }
                get injector() {
                    return this._injector
                }
                destroy() {
                    if (this._destroyed)
                        throw new M(404,"");
                    this._modules.slice().forEach(r=>r.destroy()),
                    this._destroyListeners.forEach(r=>r());
                    const t = this._injector.get(l_, null);
                    null == t || t(),
                    this._destroyed = !0
                }
                get destroyed() {
                    return this._destroyed
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(vt))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "platform"
            }),
            n
        }
        )();
        function d_(n, e) {
            return Array.isArray(e) ? e.reduce(d_, n) : Object.assign(Object.assign({}, n), e)
        }
        let f_ = (()=>{
            class n {
                constructor(t, r, i, o) {
                    this._zone = t,
                    this._injector = r,
                    this._exceptionHandler = i,
                    this._initStatus = o,
                    this._bootstrapListeners = [],
                    this._views = [],
                    this._runningTick = !1,
                    this._stable = !0,
                    this.componentTypes = [],
                    this.components = [],
                    this._onMicrotaskEmptySubscription = this._zone.onMicrotaskEmpty.subscribe({
                        next: ()=>{
                            this._zone.run(()=>{
                                this.tick()
                            }
                            )
                        }
                    });
                    const s = new Fe(l=>{
                        this._stable = this._zone.isStable && !this._zone.hasPendingMacrotasks && !this._zone.hasPendingMicrotasks,
                        this._zone.runOutsideAngular(()=>{
                            l.next(this._stable),
                            l.complete()
                        }
                        )
                    }
                    )
                      , a = new Fe(l=>{
                        let u;
                        this._zone.runOutsideAngular(()=>{
                            u = this._zone.onStable.subscribe(()=>{
                                _e.assertNotInAngularZone(),
                                Lc(()=>{
                                    !this._stable && !this._zone.hasPendingMacrotasks && !this._zone.hasPendingMicrotasks && (this._stable = !0,
                                    l.next(!0))
                                }
                                )
                            }
                            )
                        }
                        );
                        const c = this._zone.onUnstable.subscribe(()=>{
                            _e.assertInAngularZone(),
                            this._stable && (this._stable = !1,
                            this._zone.runOutsideAngular(()=>{
                                l.next(!1)
                            }
                            ))
                        }
                        );
                        return ()=>{
                            u.unsubscribe(),
                            c.unsubscribe()
                        }
                    }
                    );
                    this.isStable = Qf(s, a.pipe(Zf()))
                }
                bootstrap(t, r) {
                    if (!this._initStatus.done)
                        throw new M(405,"");
                    let i;
                    i = t instanceof by ? t : this._injector.get(qs).resolveComponentFactory(t),
                    this.componentTypes.push(i.componentType);
                    const o = function jS(n) {
                        return n.isBoundToModule
                    }(i) ? void 0 : this._injector.get(_i)
                      , a = i.create(vt.NULL, [], r || i.selector, o)
                      , l = a.location.nativeElement
                      , u = a.injector.get(jc, null)
                      , c = u && a.injector.get(PS);
                    return u && c && c.registerApplication(l, u),
                    a.onDestroy(()=>{
                        this.detachView(a.hostView),
                        $c(this.components, a),
                        c && c.unregisterApplication(l)
                    }
                    ),
                    this._loadComponent(a),
                    a
                }
                tick() {
                    if (this._runningTick)
                        throw new M(101,"");
                    try {
                        this._runningTick = !0;
                        for (let t of this._views)
                            t.detectChanges()
                    } catch (t) {
                        this._zone.runOutsideAngular(()=>this._exceptionHandler.handleError(t))
                    } finally {
                        this._runningTick = !1
                    }
                }
                attachView(t) {
                    const r = t;
                    this._views.push(r),
                    r.attachToAppRef(this)
                }
                detachView(t) {
                    const r = t;
                    $c(this._views, r),
                    r.detachFromAppRef()
                }
                _loadComponent(t) {
                    this.attachView(t.hostView),
                    this.tick(),
                    this.components.push(t),
                    this._injector.get(MS, []).concat(this._bootstrapListeners).forEach(i=>i(t))
                }
                ngOnDestroy() {
                    this._views.slice().forEach(t=>t.destroy()),
                    this._onMicrotaskEmptySubscription.unsubscribe()
                }
                get viewCount() {
                    return this._views.length
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(_e),w(vt),w(Hn),w(Rc))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        function $c(n, e) {
            const t = n.indexOf(e);
            t > -1 && n.splice(t, 1)
        }
        let p_ = !0
          , Gc = (()=>{
            class n {
            }
            return n.__NG_ELEMENT_ID__ = KS,
            n
        }
        )();
        function KS(n) {
            return function QS(n, e, t) {
                if (ts(n) && !t) {
                    const r = pt(n.index, e);
                    return new mo(r,r)
                }
                return 47 & n.type ? new mo(e[16],e) : null
            }(Ne(), b(), 16 == (16 & n))
        }
        class v_ {
            constructor() {}
            supports(e) {
                return io(e)
            }
            create(e) {
                return new tx(e)
            }
        }
        const ex = (n,e)=>e;
        class tx {
            constructor(e) {
                this.length = 0,
                this._linkedRecords = null,
                this._unlinkedRecords = null,
                this._previousItHead = null,
                this._itHead = null,
                this._itTail = null,
                this._additionsHead = null,
                this._additionsTail = null,
                this._movesHead = null,
                this._movesTail = null,
                this._removalsHead = null,
                this._removalsTail = null,
                this._identityChangesHead = null,
                this._identityChangesTail = null,
                this._trackByFn = e || ex
            }
            forEachItem(e) {
                let t;
                for (t = this._itHead; null !== t; t = t._next)
                    e(t)
            }
            forEachOperation(e) {
                let t = this._itHead
                  , r = this._removalsHead
                  , i = 0
                  , o = null;
                for (; t || r; ) {
                    const s = !r || t && t.currentIndex < D_(r, i, o) ? t : r
                      , a = D_(s, i, o)
                      , l = s.currentIndex;
                    if (s === r)
                        i--,
                        r = r._nextRemoved;
                    else if (t = t._next,
                    null == s.previousIndex)
                        i++;
                    else {
                        o || (o = []);
                        const u = a - i
                          , c = l - i;
                        if (u != c) {
                            for (let f = 0; f < u; f++) {
                                const h = f < o.length ? o[f] : o[f] = 0
                                  , p = h + f;
                                c <= p && p < u && (o[f] = h + 1)
                            }
                            o[s.previousIndex] = c - u
                        }
                    }
                    a !== l && e(s, a, l)
                }
            }
            forEachPreviousItem(e) {
                let t;
                for (t = this._previousItHead; null !== t; t = t._nextPrevious)
                    e(t)
            }
            forEachAddedItem(e) {
                let t;
                for (t = this._additionsHead; null !== t; t = t._nextAdded)
                    e(t)
            }
            forEachMovedItem(e) {
                let t;
                for (t = this._movesHead; null !== t; t = t._nextMoved)
                    e(t)
            }
            forEachRemovedItem(e) {
                let t;
                for (t = this._removalsHead; null !== t; t = t._nextRemoved)
                    e(t)
            }
            forEachIdentityChange(e) {
                let t;
                for (t = this._identityChangesHead; null !== t; t = t._nextIdentityChange)
                    e(t)
            }
            diff(e) {
                if (null == e && (e = []),
                !io(e))
                    throw new M(900,"");
                return this.check(e) ? this : null
            }
            onDestroy() {}
            check(e) {
                this._reset();
                let i, o, s, t = this._itHead, r = !1;
                if (Array.isArray(e)) {
                    this.length = e.length;
                    for (let a = 0; a < this.length; a++)
                        o = e[a],
                        s = this._trackByFn(a, o),
                        null !== t && Object.is(t.trackById, s) ? (r && (t = this._verifyReinsertion(t, o, s, a)),
                        Object.is(t.item, o) || this._addIdentityChange(t, o)) : (t = this._mismatch(t, o, s, a),
                        r = !0),
                        t = t._next
                } else
                    i = 0,
                    function nA(n, e) {
                        if (Array.isArray(n))
                            for (let t = 0; t < n.length; t++)
                                e(n[t]);
                        else {
                            const t = n[ni()]();
                            let r;
                            for (; !(r = t.next()).done; )
                                e(r.value)
                        }
                    }(e, a=>{
                        s = this._trackByFn(i, a),
                        null !== t && Object.is(t.trackById, s) ? (r && (t = this._verifyReinsertion(t, a, s, i)),
                        Object.is(t.item, a) || this._addIdentityChange(t, a)) : (t = this._mismatch(t, a, s, i),
                        r = !0),
                        t = t._next,
                        i++
                    }
                    ),
                    this.length = i;
                return this._truncate(t),
                this.collection = e,
                this.isDirty
            }
            get isDirty() {
                return null !== this._additionsHead || null !== this._movesHead || null !== this._removalsHead || null !== this._identityChangesHead
            }
            _reset() {
                if (this.isDirty) {
                    let e;
                    for (e = this._previousItHead = this._itHead; null !== e; e = e._next)
                        e._nextPrevious = e._next;
                    for (e = this._additionsHead; null !== e; e = e._nextAdded)
                        e.previousIndex = e.currentIndex;
                    for (this._additionsHead = this._additionsTail = null,
                    e = this._movesHead; null !== e; e = e._nextMoved)
                        e.previousIndex = e.currentIndex;
                    this._movesHead = this._movesTail = null,
                    this._removalsHead = this._removalsTail = null,
                    this._identityChangesHead = this._identityChangesTail = null
                }
            }
            _mismatch(e, t, r, i) {
                let o;
                return null === e ? o = this._itTail : (o = e._prev,
                this._remove(e)),
                null !== (e = null === this._unlinkedRecords ? null : this._unlinkedRecords.get(r, null)) ? (Object.is(e.item, t) || this._addIdentityChange(e, t),
                this._reinsertAfter(e, o, i)) : null !== (e = null === this._linkedRecords ? null : this._linkedRecords.get(r, i)) ? (Object.is(e.item, t) || this._addIdentityChange(e, t),
                this._moveAfter(e, o, i)) : e = this._addAfter(new nx(t,r), o, i),
                e
            }
            _verifyReinsertion(e, t, r, i) {
                let o = null === this._unlinkedRecords ? null : this._unlinkedRecords.get(r, null);
                return null !== o ? e = this._reinsertAfter(o, e._prev, i) : e.currentIndex != i && (e.currentIndex = i,
                this._addToMoves(e, i)),
                e
            }
            _truncate(e) {
                for (; null !== e; ) {
                    const t = e._next;
                    this._addToRemovals(this._unlink(e)),
                    e = t
                }
                null !== this._unlinkedRecords && this._unlinkedRecords.clear(),
                null !== this._additionsTail && (this._additionsTail._nextAdded = null),
                null !== this._movesTail && (this._movesTail._nextMoved = null),
                null !== this._itTail && (this._itTail._next = null),
                null !== this._removalsTail && (this._removalsTail._nextRemoved = null),
                null !== this._identityChangesTail && (this._identityChangesTail._nextIdentityChange = null)
            }
            _reinsertAfter(e, t, r) {
                null !== this._unlinkedRecords && this._unlinkedRecords.remove(e);
                const i = e._prevRemoved
                  , o = e._nextRemoved;
                return null === i ? this._removalsHead = o : i._nextRemoved = o,
                null === o ? this._removalsTail = i : o._prevRemoved = i,
                this._insertAfter(e, t, r),
                this._addToMoves(e, r),
                e
            }
            _moveAfter(e, t, r) {
                return this._unlink(e),
                this._insertAfter(e, t, r),
                this._addToMoves(e, r),
                e
            }
            _addAfter(e, t, r) {
                return this._insertAfter(e, t, r),
                this._additionsTail = null === this._additionsTail ? this._additionsHead = e : this._additionsTail._nextAdded = e,
                e
            }
            _insertAfter(e, t, r) {
                const i = null === t ? this._itHead : t._next;
                return e._next = i,
                e._prev = t,
                null === i ? this._itTail = e : i._prev = e,
                null === t ? this._itHead = e : t._next = e,
                null === this._linkedRecords && (this._linkedRecords = new b_),
                this._linkedRecords.put(e),
                e.currentIndex = r,
                e
            }
            _remove(e) {
                return this._addToRemovals(this._unlink(e))
            }
            _unlink(e) {
                null !== this._linkedRecords && this._linkedRecords.remove(e);
                const t = e._prev
                  , r = e._next;
                return null === t ? this._itHead = r : t._next = r,
                null === r ? this._itTail = t : r._prev = t,
                e
            }
            _addToMoves(e, t) {
                return e.previousIndex === t || (this._movesTail = null === this._movesTail ? this._movesHead = e : this._movesTail._nextMoved = e),
                e
            }
            _addToRemovals(e) {
                return null === this._unlinkedRecords && (this._unlinkedRecords = new b_),
                this._unlinkedRecords.put(e),
                e.currentIndex = null,
                e._nextRemoved = null,
                null === this._removalsTail ? (this._removalsTail = this._removalsHead = e,
                e._prevRemoved = null) : (e._prevRemoved = this._removalsTail,
                this._removalsTail = this._removalsTail._nextRemoved = e),
                e
            }
            _addIdentityChange(e, t) {
                return e.item = t,
                this._identityChangesTail = null === this._identityChangesTail ? this._identityChangesHead = e : this._identityChangesTail._nextIdentityChange = e,
                e
            }
        }
        class nx {
            constructor(e, t) {
                this.item = e,
                this.trackById = t,
                this.currentIndex = null,
                this.previousIndex = null,
                this._nextPrevious = null,
                this._prev = null,
                this._next = null,
                this._prevDup = null,
                this._nextDup = null,
                this._prevRemoved = null,
                this._nextRemoved = null,
                this._nextAdded = null,
                this._nextMoved = null,
                this._nextIdentityChange = null
            }
        }
        class rx {
            constructor() {
                this._head = null,
                this._tail = null
            }
            add(e) {
                null === this._head ? (this._head = this._tail = e,
                e._nextDup = null,
                e._prevDup = null) : (this._tail._nextDup = e,
                e._prevDup = this._tail,
                e._nextDup = null,
                this._tail = e)
            }
            get(e, t) {
                let r;
                for (r = this._head; null !== r; r = r._nextDup)
                    if ((null === t || t <= r.currentIndex) && Object.is(r.trackById, e))
                        return r;
                return null
            }
            remove(e) {
                const t = e._prevDup
                  , r = e._nextDup;
                return null === t ? this._head = r : t._nextDup = r,
                null === r ? this._tail = t : r._prevDup = t,
                null === this._head
            }
        }
        class b_ {
            constructor() {
                this.map = new Map
            }
            put(e) {
                const t = e.trackById;
                let r = this.map.get(t);
                r || (r = new rx,
                this.map.set(t, r)),
                r.add(e)
            }
            get(e, t) {
                const i = this.map.get(e);
                return i ? i.get(e, t) : null
            }
            remove(e) {
                const t = e.trackById;
                return this.map.get(t).remove(e) && this.map.delete(t),
                e
            }
            get isEmpty() {
                return 0 === this.map.size
            }
            clear() {
                this.map.clear()
            }
        }
        function D_(n, e, t) {
            const r = n.previousIndex;
            if (null === r)
                return r;
            let i = 0;
            return t && r < t.length && (i = t[r]),
            r + e + i
        }
        function E_() {
            return new ta([new v_])
        }
        let ta = (()=>{
            class n {
                constructor(t) {
                    this.factories = t
                }
                static create(t, r) {
                    if (null != r) {
                        const i = r.factories.slice();
                        t = t.concat(i)
                    }
                    return new n(t)
                }
                static extend(t) {
                    return {
                        provide: n,
                        useFactory: r=>n.create(t, r || E_()),
                        deps: [[n, new Wi, new ur]]
                    }
                }
                find(t) {
                    const r = this.factories.find(i=>i.supports(t));
                    if (null != r)
                        return r;
                    throw new M(901,"")
                }
            }
            return n.\u0275prov = R({
                token: n,
                providedIn: "root",
                factory: E_
            }),
            n
        }
        )();
        const lx = u_(null, "core", []);
        let ux = (()=>{
            class n {
                constructor(t) {}
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(f_))
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({}),
            n
        }
        )()
          , na = null;
        function vr() {
            return na
        }
        const ge = new S("DocumentToken");
        function R_(n, e) {
            e = encodeURIComponent(e);
            for (const t of n.split(";")) {
                const r = t.indexOf("=")
                  , [i,o] = -1 == r ? [t, ""] : [t.slice(0, r), t.slice(r + 1)];
                if (i.trim() === e)
                    return decodeURIComponent(o)
            }
            return null
        }
        class eF {
            constructor(e, t, r, i) {
                this.$implicit = e,
                this.ngForOf = t,
                this.index = r,
                this.count = i
            }
            get first() {
                return 0 === this.index
            }
            get last() {
                return this.index === this.count - 1
            }
            get even() {
                return this.index % 2 == 0
            }
            get odd() {
                return !this.even
            }
        }
        let P_ = (()=>{
            class n {
                constructor(t, r, i) {
                    this._viewContainer = t,
                    this._template = r,
                    this._differs = i,
                    this._ngForOf = null,
                    this._ngForOfDirty = !0,
                    this._differ = null
                }
                set ngForOf(t) {
                    this._ngForOf = t,
                    this._ngForOfDirty = !0
                }
                set ngForTrackBy(t) {
                    this._trackByFn = t
                }
                get ngForTrackBy() {
                    return this._trackByFn
                }
                set ngForTemplate(t) {
                    t && (this._template = t)
                }
                ngDoCheck() {
                    if (this._ngForOfDirty) {
                        this._ngForOfDirty = !1;
                        const t = this._ngForOf;
                        !this._differ && t && (this._differ = this._differs.find(t).create(this.ngForTrackBy))
                    }
                    if (this._differ) {
                        const t = this._differ.diff(this._ngForOf);
                        t && this._applyChanges(t)
                    }
                }
                _applyChanges(t) {
                    const r = this._viewContainer;
                    t.forEachOperation((i,o,s)=>{
                        if (null == i.previousIndex)
                            r.createEmbeddedView(this._template, new eF(i.item,this._ngForOf,-1,-1), null === s ? void 0 : s);
                        else if (null == s)
                            r.remove(null === o ? void 0 : o);
                        else if (null !== o) {
                            const a = r.get(o);
                            r.move(a, s),
                            L_(a, i)
                        }
                    }
                    );
                    for (let i = 0, o = r.length; i < o; i++) {
                        const a = r.get(i).context;
                        a.index = i,
                        a.count = o,
                        a.ngForOf = this._ngForOf
                    }
                    t.forEachIdentityChange(i=>{
                        L_(r.get(i.currentIndex), i)
                    }
                    )
                }
                static ngTemplateContextGuard(t, r) {
                    return !0
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(yn),v(Tn),v(ta))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "ngFor", "", "ngForOf", ""]],
                inputs: {
                    ngForOf: "ngForOf",
                    ngForTrackBy: "ngForTrackBy",
                    ngForTemplate: "ngForTemplate"
                }
            }),
            n
        }
        )();
        function L_(n, e) {
            n.context.$implicit = e.item
        }
        let V_ = (()=>{
            class n {
                constructor(t, r) {
                    this._viewContainer = t,
                    this._context = new tF,
                    this._thenTemplateRef = null,
                    this._elseTemplateRef = null,
                    this._thenViewRef = null,
                    this._elseViewRef = null,
                    this._thenTemplateRef = r
                }
                set ngIf(t) {
                    this._context.$implicit = this._context.ngIf = t,
                    this._updateView()
                }
                set ngIfThen(t) {
                    B_("ngIfThen", t),
                    this._thenTemplateRef = t,
                    this._thenViewRef = null,
                    this._updateView()
                }
                set ngIfElse(t) {
                    B_("ngIfElse", t),
                    this._elseTemplateRef = t,
                    this._elseViewRef = null,
                    this._updateView()
                }
                _updateView() {
                    this._context.$implicit ? this._thenViewRef || (this._viewContainer.clear(),
                    this._elseViewRef = null,
                    this._thenTemplateRef && (this._thenViewRef = this._viewContainer.createEmbeddedView(this._thenTemplateRef, this._context))) : this._elseViewRef || (this._viewContainer.clear(),
                    this._thenViewRef = null,
                    this._elseTemplateRef && (this._elseViewRef = this._viewContainer.createEmbeddedView(this._elseTemplateRef, this._context)))
                }
                static ngTemplateContextGuard(t, r) {
                    return !0
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(yn),v(Tn))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "ngIf", ""]],
                inputs: {
                    ngIf: "ngIf",
                    ngIfThen: "ngIfThen",
                    ngIfElse: "ngIfElse"
                }
            }),
            n
        }
        )();
        class tF {
            constructor() {
                this.$implicit = null,
                this.ngIf = null
            }
        }
        function B_(n, e) {
            if (e && !e.createEmbeddedView)
                throw new Error(`${n} must be a TemplateRef, but received '${te(e)}'.`)
        }
        class id {
            constructor(e, t) {
                this._viewContainerRef = e,
                this._templateRef = t,
                this._created = !1
            }
            create() {
                this._created = !0,
                this._viewContainerRef.createEmbeddedView(this._templateRef)
            }
            destroy() {
                this._created = !1,
                this._viewContainerRef.clear()
            }
            enforceState(e) {
                e && !this._created ? this.create() : !e && this._created && this.destroy()
            }
        }
        let fa = (()=>{
            class n {
                constructor() {
                    this._defaultUsed = !1,
                    this._caseCount = 0,
                    this._lastCaseCheckIndex = 0,
                    this._lastCasesMatched = !1
                }
                set ngSwitch(t) {
                    this._ngSwitch = t,
                    0 === this._caseCount && this._updateDefaultCases(!0)
                }
                _addCase() {
                    return this._caseCount++
                }
                _addDefault(t) {
                    this._defaultViews || (this._defaultViews = []),
                    this._defaultViews.push(t)
                }
                _matchCase(t) {
                    const r = t == this._ngSwitch;
                    return this._lastCasesMatched = this._lastCasesMatched || r,
                    this._lastCaseCheckIndex++,
                    this._lastCaseCheckIndex === this._caseCount && (this._updateDefaultCases(!this._lastCasesMatched),
                    this._lastCaseCheckIndex = 0,
                    this._lastCasesMatched = !1),
                    r
                }
                _updateDefaultCases(t) {
                    if (this._defaultViews && t !== this._defaultUsed) {
                        this._defaultUsed = t;
                        for (let r = 0; r < this._defaultViews.length; r++)
                            this._defaultViews[r].enforceState(t)
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "ngSwitch", ""]],
                inputs: {
                    ngSwitch: "ngSwitch"
                }
            }),
            n
        }
        )()
          , j_ = (()=>{
            class n {
                constructor(t, r, i) {
                    this.ngSwitch = i,
                    i._addCase(),
                    this._view = new id(t,r)
                }
                ngDoCheck() {
                    this._view.enforceState(this.ngSwitch._matchCase(this.ngSwitchCase))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(yn),v(Tn),v(fa, 9))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "ngSwitchCase", ""]],
                inputs: {
                    ngSwitchCase: "ngSwitchCase"
                }
            }),
            n
        }
        )()
          , $_ = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({}),
            n
        }
        )();
        const G_ = "browser";
        class q_ {
        }
        class ad extends class NF extends class fx {
        }
        {
            constructor() {
                super(...arguments),
                this.supportsDOMEvents = !0
            }
        }
        {
            static makeCurrent() {
                !function dx(n) {
                    na || (na = n)
                }(new ad)
            }
            onAndCancel(e, t, r) {
                return e.addEventListener(t, r, !1),
                ()=>{
                    e.removeEventListener(t, r, !1)
                }
            }
            dispatchEvent(e, t) {
                e.dispatchEvent(t)
            }
            remove(e) {
                e.parentNode && e.parentNode.removeChild(e)
            }
            createElement(e, t) {
                return (t = t || this.getDefaultDocument()).createElement(e)
            }
            createHtmlDocument() {
                return document.implementation.createHTMLDocument("fakeTitle")
            }
            getDefaultDocument() {
                return document
            }
            isElementNode(e) {
                return e.nodeType === Node.ELEMENT_NODE
            }
            isShadowRoot(e) {
                return e instanceof DocumentFragment
            }
            getGlobalEventTarget(e, t) {
                return "window" === t ? window : "document" === t ? e : "body" === t ? e.body : null
            }
            getBaseHref(e) {
                const t = function OF() {
                    return wo = wo || document.querySelector("base"),
                    wo ? wo.getAttribute("href") : null
                }();
                return null == t ? null : function kF(n) {
                    ha = ha || document.createElement("a"),
                    ha.setAttribute("href", n);
                    const e = ha.pathname;
                    return "/" === e.charAt(0) ? e : `/${e}`
                }(t)
            }
            resetBaseElement() {
                wo = null
            }
            getUserAgent() {
                return window.navigator.userAgent
            }
            getCookie(e) {
                return R_(document.cookie, e)
            }
        }
        let ha, wo = null;
        const W_ = new S("TRANSITION_ID")
          , PF = [{
            provide: n_,
            useFactory: function RF(n, e, t) {
                return ()=>{
                    t.get(Rc).donePromise.then(()=>{
                        const r = vr()
                          , i = e.querySelectorAll(`style[ng-transition="${n}"]`);
                        for (let o = 0; o < i.length; o++)
                            r.remove(i[o])
                    }
                    )
                }
            },
            deps: [W_, ge, vt],
            multi: !0
        }];
        class ld {
            static init() {
                !function VS(n) {
                    Hc = n
                }(new ld)
            }
            addToWindow(e) {
                ne.getAngularTestability = (r,i=!0)=>{
                    const o = e.findTestabilityInTree(r, i);
                    if (null == o)
                        throw new Error("Could not find testability for element.");
                    return o
                }
                ,
                ne.getAllAngularTestabilities = ()=>e.getAllTestabilities(),
                ne.getAllAngularRootElements = ()=>e.getAllRootElements(),
                ne.frameworkStabilizers || (ne.frameworkStabilizers = []),
                ne.frameworkStabilizers.push(r=>{
                    const i = ne.getAllAngularTestabilities();
                    let o = i.length
                      , s = !1;
                    const a = function(l) {
                        s = s || l,
                        o--,
                        0 == o && r(s)
                    };
                    i.forEach(function(l) {
                        l.whenStable(a)
                    })
                }
                )
            }
            findTestabilityInTree(e, t, r) {
                if (null == t)
                    return null;
                const i = e.getTestability(t);
                return null != i ? i : r ? vr().isShadowRoot(t) ? this.findTestabilityInTree(e, t.host, !0) : this.findTestabilityInTree(e, t.parentElement, !0) : null
            }
        }
        let LF = (()=>{
            class n {
                build() {
                    return new XMLHttpRequest
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        const pa = new S("EventManagerPlugins");
        let ma = (()=>{
            class n {
                constructor(t, r) {
                    this._zone = r,
                    this._eventNameToPlugin = new Map,
                    t.forEach(i=>i.manager = this),
                    this._plugins = t.slice().reverse()
                }
                addEventListener(t, r, i) {
                    return this._findPluginFor(r).addEventListener(t, r, i)
                }
                addGlobalEventListener(t, r, i) {
                    return this._findPluginFor(r).addGlobalEventListener(t, r, i)
                }
                getZone() {
                    return this._zone
                }
                _findPluginFor(t) {
                    const r = this._eventNameToPlugin.get(t);
                    if (r)
                        return r;
                    const i = this._plugins;
                    for (let o = 0; o < i.length; o++) {
                        const s = i[o];
                        if (s.supports(t))
                            return this._eventNameToPlugin.set(t, s),
                            s
                    }
                    throw new Error(`No event manager plugin found for event ${t}`)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(pa),w(_e))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        class K_ {
            constructor(e) {
                this._doc = e
            }
            addGlobalEventListener(e, t, r) {
                const i = vr().getGlobalEventTarget(this._doc, e);
                if (!i)
                    throw new Error(`Unsupported event target ${i} for event ${t}`);
                return this.addEventListener(i, t, r)
            }
        }
        let Q_ = (()=>{
            class n {
                constructor() {
                    this._stylesSet = new Set
                }
                addStyles(t) {
                    const r = new Set;
                    t.forEach(i=>{
                        this._stylesSet.has(i) || (this._stylesSet.add(i),
                        r.add(i))
                    }
                    ),
                    this.onStylesAdded(r)
                }
                onStylesAdded(t) {}
                getAllStyles() {
                    return Array.from(this._stylesSet)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )()
          , Mo = (()=>{
            class n extends Q_ {
                constructor(t) {
                    super(),
                    this._doc = t,
                    this._hostNodes = new Map,
                    this._hostNodes.set(t.head, [])
                }
                _addStylesToHost(t, r, i) {
                    t.forEach(o=>{
                        const s = this._doc.createElement("style");
                        s.textContent = o,
                        i.push(r.appendChild(s))
                    }
                    )
                }
                addHost(t) {
                    const r = [];
                    this._addStylesToHost(this._stylesSet, t, r),
                    this._hostNodes.set(t, r)
                }
                removeHost(t) {
                    const r = this._hostNodes.get(t);
                    r && r.forEach(Z_),
                    this._hostNodes.delete(t)
                }
                onStylesAdded(t) {
                    this._hostNodes.forEach((r,i)=>{
                        this._addStylesToHost(t, i, r)
                    }
                    )
                }
                ngOnDestroy() {
                    this._hostNodes.forEach(t=>t.forEach(Z_))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(ge))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        function Z_(n) {
            vr().remove(n)
        }
        const ud = {
            svg: "http://www.w3.org/2000/svg",
            xhtml: "http://www.w3.org/1999/xhtml",
            xlink: "http://www.w3.org/1999/xlink",
            xml: "http://www.w3.org/XML/1998/namespace",
            xmlns: "http://www.w3.org/2000/xmlns/",
            math: "http://www.w3.org/1998/MathML/"
        }
          , cd = /%COMP%/g;
        function ga(n, e, t) {
            for (let r = 0; r < e.length; r++) {
                let i = e[r];
                Array.isArray(i) ? ga(n, i, t) : (i = i.replace(cd, n),
                t.push(i))
            }
            return t
        }
        function J_(n) {
            return e=>{
                if ("__ngUnwrap__" === e)
                    return n;
                !1 === n(e) && (e.preventDefault(),
                e.returnValue = !1)
            }
        }
        let ya = (()=>{
            class n {
                constructor(t, r, i) {
                    this.eventManager = t,
                    this.sharedStylesHost = r,
                    this.appId = i,
                    this.rendererByCompId = new Map,
                    this.defaultRenderer = new dd(t)
                }
                createRenderer(t, r) {
                    if (!t || !r)
                        return this.defaultRenderer;
                    switch (r.encapsulation) {
                    case Gt.Emulated:
                        {
                            let i = this.rendererByCompId.get(r.id);
                            return i || (i = new $F(this.eventManager,this.sharedStylesHost,r,this.appId),
                            this.rendererByCompId.set(r.id, i)),
                            i.applyToHost(t),
                            i
                        }
                    case 1:
                    case Gt.ShadowDom:
                        return new GF(this.eventManager,this.sharedStylesHost,t,r);
                    default:
                        if (!this.rendererByCompId.has(r.id)) {
                            const i = ga(r.id, r.styles, []);
                            this.sharedStylesHost.addStyles(i),
                            this.rendererByCompId.set(r.id, this.defaultRenderer)
                        }
                        return this.defaultRenderer
                    }
                }
                begin() {}
                end() {}
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(ma),w(Mo),w(bo))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        class dd {
            constructor(e) {
                this.eventManager = e,
                this.data = Object.create(null),
                this.destroyNode = null
            }
            destroy() {}
            createElement(e, t) {
                return t ? document.createElementNS(ud[t] || t, e) : document.createElement(e)
            }
            createComment(e) {
                return document.createComment(e)
            }
            createText(e) {
                return document.createTextNode(e)
            }
            appendChild(e, t) {
                e.appendChild(t)
            }
            insertBefore(e, t, r) {
                e && e.insertBefore(t, r)
            }
            removeChild(e, t) {
                e && e.removeChild(t)
            }
            selectRootElement(e, t) {
                let r = "string" == typeof e ? document.querySelector(e) : e;
                if (!r)
                    throw new Error(`The selector "${e}" did not match any elements`);
                return t || (r.textContent = ""),
                r
            }
            parentNode(e) {
                return e.parentNode
            }
            nextSibling(e) {
                return e.nextSibling
            }
            setAttribute(e, t, r, i) {
                if (i) {
                    t = i + ":" + t;
                    const o = ud[i];
                    o ? e.setAttributeNS(o, t, r) : e.setAttribute(t, r)
                } else
                    e.setAttribute(t, r)
            }
            removeAttribute(e, t, r) {
                if (r) {
                    const i = ud[r];
                    i ? e.removeAttributeNS(i, t) : e.removeAttribute(`${r}:${t}`)
                } else
                    e.removeAttribute(t)
            }
            addClass(e, t) {
                e.classList.add(t)
            }
            removeClass(e, t) {
                e.classList.remove(t)
            }
            setStyle(e, t, r, i) {
                i & (yt.DashCase | yt.Important) ? e.style.setProperty(t, r, i & yt.Important ? "important" : "") : e.style[t] = r
            }
            removeStyle(e, t, r) {
                r & yt.DashCase ? e.style.removeProperty(t) : e.style[t] = ""
            }
            setProperty(e, t, r) {
                e[t] = r
            }
            setValue(e, t) {
                e.nodeValue = t
            }
            listen(e, t, r) {
                return "string" == typeof e ? this.eventManager.addGlobalEventListener(e, t, J_(r)) : this.eventManager.addEventListener(e, t, J_(r))
            }
        }
        class $F extends dd {
            constructor(e, t, r, i) {
                super(e),
                this.component = r;
                const o = ga(i + "-" + r.id, r.styles, []);
                t.addStyles(o),
                this.contentAttr = function jF(n) {
                    return "_ngcontent-%COMP%".replace(cd, n)
                }(i + "-" + r.id),
                this.hostAttr = function HF(n) {
                    return "_nghost-%COMP%".replace(cd, n)
                }(i + "-" + r.id)
            }
            applyToHost(e) {
                super.setAttribute(e, this.hostAttr, "")
            }
            createElement(e, t) {
                const r = super.createElement(e, t);
                return super.setAttribute(r, this.contentAttr, ""),
                r
            }
        }
        class GF extends dd {
            constructor(e, t, r, i) {
                super(e),
                this.sharedStylesHost = t,
                this.hostEl = r,
                this.shadowRoot = r.attachShadow({
                    mode: "open"
                }),
                this.sharedStylesHost.addHost(this.shadowRoot);
                const o = ga(i.id, i.styles, []);
                for (let s = 0; s < o.length; s++) {
                    const a = document.createElement("style");
                    a.textContent = o[s],
                    this.shadowRoot.appendChild(a)
                }
            }
            nodeOrShadowRoot(e) {
                return e === this.hostEl ? this.shadowRoot : e
            }
            destroy() {
                this.sharedStylesHost.removeHost(this.shadowRoot)
            }
            appendChild(e, t) {
                return super.appendChild(this.nodeOrShadowRoot(e), t)
            }
            insertBefore(e, t, r) {
                return super.insertBefore(this.nodeOrShadowRoot(e), t, r)
            }
            removeChild(e, t) {
                return super.removeChild(this.nodeOrShadowRoot(e), t)
            }
            parentNode(e) {
                return this.nodeOrShadowRoot(super.parentNode(this.nodeOrShadowRoot(e)))
            }
        }
        let zF = (()=>{
            class n extends K_ {
                constructor(t) {
                    super(t)
                }
                supports(t) {
                    return !0
                }
                addEventListener(t, r, i) {
                    return t.addEventListener(r, i, !1),
                    ()=>this.removeEventListener(t, r, i)
                }
                removeEventListener(t, r, i) {
                    return t.removeEventListener(r, i)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(ge))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        const tv = ["alt", "control", "meta", "shift"]
          , WF = {
            "\b": "Backspace",
            "\t": "Tab",
            "\x7f": "Delete",
            "\x1b": "Escape",
            Del: "Delete",
            Esc: "Escape",
            Left: "ArrowLeft",
            Right: "ArrowRight",
            Up: "ArrowUp",
            Down: "ArrowDown",
            Menu: "ContextMenu",
            Scroll: "ScrollLock",
            Win: "OS"
        }
          , nv = {
            A: "1",
            B: "2",
            C: "3",
            D: "4",
            E: "5",
            F: "6",
            G: "7",
            H: "8",
            I: "9",
            J: "*",
            K: "+",
            M: "-",
            N: ".",
            O: "/",
            "`": "0",
            "\x90": "NumLock"
        }
          , KF = {
            alt: n=>n.altKey,
            control: n=>n.ctrlKey,
            meta: n=>n.metaKey,
            shift: n=>n.shiftKey
        };
        let QF = (()=>{
            class n extends K_ {
                constructor(t) {
                    super(t)
                }
                supports(t) {
                    return null != n.parseEventName(t)
                }
                addEventListener(t, r, i) {
                    const o = n.parseEventName(r)
                      , s = n.eventCallback(o.fullKey, i, this.manager.getZone());
                    return this.manager.getZone().runOutsideAngular(()=>vr().onAndCancel(t, o.domEventName, s))
                }
                static parseEventName(t) {
                    const r = t.toLowerCase().split(".")
                      , i = r.shift();
                    if (0 === r.length || "keydown" !== i && "keyup" !== i)
                        return null;
                    const o = n._normalizeKey(r.pop());
                    let s = "";
                    if (tv.forEach(l=>{
                        const u = r.indexOf(l);
                        u > -1 && (r.splice(u, 1),
                        s += l + ".")
                    }
                    ),
                    s += o,
                    0 != r.length || 0 === o.length)
                        return null;
                    const a = {};
                    return a.domEventName = i,
                    a.fullKey = s,
                    a
                }
                static getEventFullKey(t) {
                    let r = ""
                      , i = function ZF(n) {
                        let e = n.key;
                        if (null == e) {
                            if (e = n.keyIdentifier,
                            null == e)
                                return "Unidentified";
                            e.startsWith("U+") && (e = String.fromCharCode(parseInt(e.substring(2), 16)),
                            3 === n.location && nv.hasOwnProperty(e) && (e = nv[e]))
                        }
                        return WF[e] || e
                    }(t);
                    return i = i.toLowerCase(),
                    " " === i ? i = "space" : "." === i && (i = "dot"),
                    tv.forEach(o=>{
                        o != i && KF[o](t) && (r += o + ".")
                    }
                    ),
                    r += i,
                    r
                }
                static eventCallback(t, r, i) {
                    return o=>{
                        n.getEventFullKey(o) === t && i.runGuarded(()=>r(o))
                    }
                }
                static _normalizeKey(t) {
                    return "esc" === t ? "escape" : t
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(ge))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        const eN = u_(lx, "browser", [{
            provide: Xs,
            useValue: G_
        }, {
            provide: i_,
            useValue: function YF() {
                ad.makeCurrent(),
                ld.init()
            },
            multi: !0
        }, {
            provide: ge,
            useFactory: function JF() {
                return function dE(n) {
                    Ol = n
                }(document),
                document
            },
            deps: []
        }])
          , tN = [{
            provide: Qu,
            useValue: "root"
        }, {
            provide: Hn,
            useFactory: function XF() {
                return new Hn
            },
            deps: []
        }, {
            provide: pa,
            useClass: zF,
            multi: !0,
            deps: [ge, _e, Xs]
        }, {
            provide: pa,
            useClass: QF,
            multi: !0,
            deps: [ge]
        }, {
            provide: ya,
            useClass: ya,
            deps: [ma, Mo, bo]
        }, {
            provide: po,
            useExisting: ya
        }, {
            provide: Q_,
            useExisting: Mo
        }, {
            provide: Mo,
            useClass: Mo,
            deps: [ge]
        }, {
            provide: jc,
            useClass: jc,
            deps: [_e]
        }, {
            provide: ma,
            useClass: ma,
            deps: [pa, _e]
        }, {
            provide: q_,
            useClass: LF,
            deps: []
        }];
        let rv = (()=>{
            class n {
                constructor(t) {
                    if (t)
                        throw new Error("BrowserModule has already been loaded. If you need access to common directives such as NgIf and NgFor from a lazy loaded module, import CommonModule instead.")
                }
                static withServerTransition(t) {
                    return {
                        ngModule: n,
                        providers: [{
                            provide: bo,
                            useValue: t.appId
                        }, {
                            provide: W_,
                            useExisting: bo
                        }, PF]
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(n, 12))
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                providers: tN,
                imports: [$_, ux]
            }),
            n
        }
        )();
        "undefined" != typeof window && window;
        let hd = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: function(t) {
                    let r = null;
                    return r = t ? new (t || n) : w(sv),
                    r
                },
                providedIn: "root"
            }),
            n
        }
        )()
          , sv = (()=>{
            class n extends hd {
                constructor(t) {
                    super(),
                    this._doc = t
                }
                sanitize(t, r) {
                    if (null == r)
                        return null;
                    switch (t) {
                    case ee.NONE:
                        return r;
                    case ee.HTML:
                        return un(r, "HTML") ? gt(r) : sp(this._doc, String(r)).toString();
                    case ee.STYLE:
                        return un(r, "Style") ? gt(r) : r;
                    case ee.SCRIPT:
                        if (un(r, "Script"))
                            return gt(r);
                        throw new Error("unsafe value used in a script context");
                    case ee.URL:
                        return Xh(r),
                        un(r, "URL") ? gt(r) : Qi(String(r));
                    case ee.RESOURCE_URL:
                        if (un(r, "ResourceURL"))
                            return gt(r);
                        throw new Error("unsafe value used in a resource URL context (see https://g.co/ng/security#xss)");
                    default:
                        throw new Error(`Unexpected SecurityContext ${t} (see https://g.co/ng/security#xss)`)
                    }
                }
                bypassSecurityTrustHtml(t) {
                    return function ww(n) {
                        return new vw(n)
                    }(t)
                }
                bypassSecurityTrustStyle(t) {
                    return function Mw(n) {
                        return new bw(n)
                    }(t)
                }
                bypassSecurityTrustScript(t) {
                    return function Aw(n) {
                        return new Dw(n)
                    }(t)
                }
                bypassSecurityTrustUrl(t) {
                    return function Tw(n) {
                        return new Cw(n)
                    }(t)
                }
                bypassSecurityTrustResourceUrl(t) {
                    return function Iw(n) {
                        return new Ew(n)
                    }(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(ge))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: function(t) {
                    let r = null;
                    return r = t ? new t : function dN(n) {
                        return new sv(n.get(ge))
                    }(w(vt)),
                    r
                },
                providedIn: "root"
            }),
            n
        }
        )();
        function br(...n) {
            return Fi(n, Ko(n))
        }
        function av(n, e) {
            return st((t,r)=>{
                let i = 0;
                t.subscribe(St(r, o=>n.call(e, o, i++) && r.next(o)))
            }
            )
        }
        class lv {
        }
        class uv {
        }
        class xn {
            constructor(e) {
                this.normalizedNames = new Map,
                this.lazyUpdate = null,
                e ? this.lazyInit = "string" == typeof e ? ()=>{
                    this.headers = new Map,
                    e.split("\n").forEach(t=>{
                        const r = t.indexOf(":");
                        if (r > 0) {
                            const i = t.slice(0, r)
                              , o = i.toLowerCase()
                              , s = t.slice(r + 1).trim();
                            this.maybeSetNormalizedName(i, o),
                            this.headers.has(o) ? this.headers.get(o).push(s) : this.headers.set(o, [s])
                        }
                    }
                    )
                }
                : ()=>{
                    this.headers = new Map,
                    Object.keys(e).forEach(t=>{
                        let r = e[t];
                        const i = t.toLowerCase();
                        "string" == typeof r && (r = [r]),
                        r.length > 0 && (this.headers.set(i, r),
                        this.maybeSetNormalizedName(t, i))
                    }
                    )
                }
                : this.headers = new Map
            }
            has(e) {
                return this.init(),
                this.headers.has(e.toLowerCase())
            }
            get(e) {
                this.init();
                const t = this.headers.get(e.toLowerCase());
                return t && t.length > 0 ? t[0] : null
            }
            keys() {
                return this.init(),
                Array.from(this.normalizedNames.values())
            }
            getAll(e) {
                return this.init(),
                this.headers.get(e.toLowerCase()) || null
            }
            append(e, t) {
                return this.clone({
                    name: e,
                    value: t,
                    op: "a"
                })
            }
            set(e, t) {
                return this.clone({
                    name: e,
                    value: t,
                    op: "s"
                })
            }
            delete(e, t) {
                return this.clone({
                    name: e,
                    value: t,
                    op: "d"
                })
            }
            maybeSetNormalizedName(e, t) {
                this.normalizedNames.has(t) || this.normalizedNames.set(t, e)
            }
            init() {
                this.lazyInit && (this.lazyInit instanceof xn ? this.copyFrom(this.lazyInit) : this.lazyInit(),
                this.lazyInit = null,
                this.lazyUpdate && (this.lazyUpdate.forEach(e=>this.applyUpdate(e)),
                this.lazyUpdate = null))
            }
            copyFrom(e) {
                e.init(),
                Array.from(e.headers.keys()).forEach(t=>{
                    this.headers.set(t, e.headers.get(t)),
                    this.normalizedNames.set(t, e.normalizedNames.get(t))
                }
                )
            }
            clone(e) {
                const t = new xn;
                return t.lazyInit = this.lazyInit && this.lazyInit instanceof xn ? this.lazyInit : this,
                t.lazyUpdate = (this.lazyUpdate || []).concat([e]),
                t
            }
            applyUpdate(e) {
                const t = e.name.toLowerCase();
                switch (e.op) {
                case "a":
                case "s":
                    let r = e.value;
                    if ("string" == typeof r && (r = [r]),
                    0 === r.length)
                        return;
                    this.maybeSetNormalizedName(e.name, t);
                    const i = ("a" === e.op ? this.headers.get(t) : void 0) || [];
                    i.push(...r),
                    this.headers.set(t, i);
                    break;
                case "d":
                    const o = e.value;
                    if (o) {
                        let s = this.headers.get(t);
                        if (!s)
                            return;
                        s = s.filter(a=>-1 === o.indexOf(a)),
                        0 === s.length ? (this.headers.delete(t),
                        this.normalizedNames.delete(t)) : this.headers.set(t, s)
                    } else
                        this.headers.delete(t),
                        this.normalizedNames.delete(t)
                }
            }
            forEach(e) {
                this.init(),
                Array.from(this.normalizedNames.keys()).forEach(t=>e(this.normalizedNames.get(t), this.headers.get(t)))
            }
        }
        class hN {
            encodeKey(e) {
                return cv(e)
            }
            encodeValue(e) {
                return cv(e)
            }
            decodeKey(e) {
                return decodeURIComponent(e)
            }
            decodeValue(e) {
                return decodeURIComponent(e)
            }
        }
        const mN = /%(\d[a-f0-9])/gi
          , gN = {
            40: "@",
            "3A": ":",
            24: "$",
            "2C": ",",
            "3B": ";",
            "2B": "+",
            "3D": "=",
            "3F": "?",
            "2F": "/"
        };
        function cv(n) {
            return encodeURIComponent(n).replace(mN, (e,t)=>{
                var r;
                return null !== (r = gN[t]) && void 0 !== r ? r : e
            }
            )
        }
        function dv(n) {
            return `${n}`
        }
        class zn {
            constructor(e={}) {
                if (this.updates = null,
                this.cloneFrom = null,
                this.encoder = e.encoder || new hN,
                e.fromString) {
                    if (e.fromObject)
                        throw new Error("Cannot specify both fromString and fromObject.");
                    this.map = function pN(n, e) {
                        const t = new Map;
                        return n.length > 0 && n.replace(/^\?/, "").split("&").forEach(i=>{
                            const o = i.indexOf("=")
                              , [s,a] = -1 == o ? [e.decodeKey(i), ""] : [e.decodeKey(i.slice(0, o)), e.decodeValue(i.slice(o + 1))]
                              , l = t.get(s) || [];
                            l.push(a),
                            t.set(s, l)
                        }
                        ),
                        t
                    }(e.fromString, this.encoder)
                } else
                    e.fromObject ? (this.map = new Map,
                    Object.keys(e.fromObject).forEach(t=>{
                        const r = e.fromObject[t];
                        this.map.set(t, Array.isArray(r) ? r : [r])
                    }
                    )) : this.map = null
            }
            has(e) {
                return this.init(),
                this.map.has(e)
            }
            get(e) {
                this.init();
                const t = this.map.get(e);
                return t ? t[0] : null
            }
            getAll(e) {
                return this.init(),
                this.map.get(e) || null
            }
            keys() {
                return this.init(),
                Array.from(this.map.keys())
            }
            append(e, t) {
                return this.clone({
                    param: e,
                    value: t,
                    op: "a"
                })
            }
            appendAll(e) {
                const t = [];
                return Object.keys(e).forEach(r=>{
                    const i = e[r];
                    Array.isArray(i) ? i.forEach(o=>{
                        t.push({
                            param: r,
                            value: o,
                            op: "a"
                        })
                    }
                    ) : t.push({
                        param: r,
                        value: i,
                        op: "a"
                    })
                }
                ),
                this.clone(t)
            }
            set(e, t) {
                return this.clone({
                    param: e,
                    value: t,
                    op: "s"
                })
            }
            delete(e, t) {
                return this.clone({
                    param: e,
                    value: t,
                    op: "d"
                })
            }
            toString() {
                return this.init(),
                this.keys().map(e=>{
                    const t = this.encoder.encodeKey(e);
                    return this.map.get(e).map(r=>t + "=" + this.encoder.encodeValue(r)).join("&")
                }
                ).filter(e=>"" !== e).join("&")
            }
            clone(e) {
                const t = new zn({
                    encoder: this.encoder
                });
                return t.cloneFrom = this.cloneFrom || this,
                t.updates = (this.updates || []).concat(e),
                t
            }
            init() {
                null === this.map && (this.map = new Map),
                null !== this.cloneFrom && (this.cloneFrom.init(),
                this.cloneFrom.keys().forEach(e=>this.map.set(e, this.cloneFrom.map.get(e))),
                this.updates.forEach(e=>{
                    switch (e.op) {
                    case "a":
                    case "s":
                        const t = ("a" === e.op ? this.map.get(e.param) : void 0) || [];
                        t.push(dv(e.value)),
                        this.map.set(e.param, t);
                        break;
                    case "d":
                        if (void 0 === e.value) {
                            this.map.delete(e.param);
                            break
                        }
                        {
                            let r = this.map.get(e.param) || [];
                            const i = r.indexOf(dv(e.value));
                            -1 !== i && r.splice(i, 1),
                            r.length > 0 ? this.map.set(e.param, r) : this.map.delete(e.param)
                        }
                    }
                }
                ),
                this.cloneFrom = this.updates = null)
            }
        }
        class yN {
            constructor() {
                this.map = new Map
            }
            set(e, t) {
                return this.map.set(e, t),
                this
            }
            get(e) {
                return this.map.has(e) || this.map.set(e, e.defaultValue()),
                this.map.get(e)
            }
            delete(e) {
                return this.map.delete(e),
                this
            }
            has(e) {
                return this.map.has(e)
            }
            keys() {
                return this.map.keys()
            }
        }
        function fv(n) {
            return "undefined" != typeof ArrayBuffer && n instanceof ArrayBuffer
        }
        function hv(n) {
            return "undefined" != typeof Blob && n instanceof Blob
        }
        function pv(n) {
            return "undefined" != typeof FormData && n instanceof FormData
        }
        class Ao {
            constructor(e, t, r, i) {
                let o;
                if (this.url = t,
                this.body = null,
                this.reportProgress = !1,
                this.withCredentials = !1,
                this.responseType = "json",
                this.method = e.toUpperCase(),
                function _N(n) {
                    switch (n) {
                    case "DELETE":
                    case "GET":
                    case "HEAD":
                    case "OPTIONS":
                    case "JSONP":
                        return !1;
                    default:
                        return !0
                    }
                }(this.method) || i ? (this.body = void 0 !== r ? r : null,
                o = i) : o = r,
                o && (this.reportProgress = !!o.reportProgress,
                this.withCredentials = !!o.withCredentials,
                o.responseType && (this.responseType = o.responseType),
                o.headers && (this.headers = o.headers),
                o.context && (this.context = o.context),
                o.params && (this.params = o.params)),
                this.headers || (this.headers = new xn),
                this.context || (this.context = new yN),
                this.params) {
                    const s = this.params.toString();
                    if (0 === s.length)
                        this.urlWithParams = t;
                    else {
                        const a = t.indexOf("?");
                        this.urlWithParams = t + (-1 === a ? "?" : a < t.length - 1 ? "&" : "") + s
                    }
                } else
                    this.params = new zn,
                    this.urlWithParams = t
            }
            serializeBody() {
                return null === this.body ? null : fv(this.body) || hv(this.body) || pv(this.body) || function vN(n) {
                    return "undefined" != typeof URLSearchParams && n instanceof URLSearchParams
                }(this.body) || "string" == typeof this.body ? this.body : this.body instanceof zn ? this.body.toString() : "object" == typeof this.body || "boolean" == typeof this.body || Array.isArray(this.body) ? JSON.stringify(this.body) : this.body.toString()
            }
            detectContentTypeHeader() {
                return null === this.body || pv(this.body) ? null : hv(this.body) ? this.body.type || null : fv(this.body) ? null : "string" == typeof this.body ? "text/plain" : this.body instanceof zn ? "application/x-www-form-urlencoded;charset=UTF-8" : "object" == typeof this.body || "number" == typeof this.body || "boolean" == typeof this.body ? "application/json" : null
            }
            clone(e={}) {
                var t;
                const r = e.method || this.method
                  , i = e.url || this.url
                  , o = e.responseType || this.responseType
                  , s = void 0 !== e.body ? e.body : this.body
                  , a = void 0 !== e.withCredentials ? e.withCredentials : this.withCredentials
                  , l = void 0 !== e.reportProgress ? e.reportProgress : this.reportProgress;
                let u = e.headers || this.headers
                  , c = e.params || this.params;
                const d = null !== (t = e.context) && void 0 !== t ? t : this.context;
                return void 0 !== e.setHeaders && (u = Object.keys(e.setHeaders).reduce((f,h)=>f.set(h, e.setHeaders[h]), u)),
                e.setParams && (c = Object.keys(e.setParams).reduce((f,h)=>f.set(h, e.setParams[h]), c)),
                new Ao(r,i,s,{
                    params: c,
                    headers: u,
                    context: d,
                    reportProgress: l,
                    responseType: o,
                    withCredentials: a
                })
            }
        }
        var xe = (()=>((xe = xe || {})[xe.Sent = 0] = "Sent",
        xe[xe.UploadProgress = 1] = "UploadProgress",
        xe[xe.ResponseHeader = 2] = "ResponseHeader",
        xe[xe.DownloadProgress = 3] = "DownloadProgress",
        xe[xe.Response = 4] = "Response",
        xe[xe.User = 5] = "User",
        xe))();
        class pd {
            constructor(e, t=200, r="OK") {
                this.headers = e.headers || new xn,
                this.status = void 0 !== e.status ? e.status : t,
                this.statusText = e.statusText || r,
                this.url = e.url || null,
                this.ok = this.status >= 200 && this.status < 300
            }
        }
        class md extends pd {
            constructor(e={}) {
                super(e),
                this.type = xe.ResponseHeader
            }
            clone(e={}) {
                return new md({
                    headers: e.headers || this.headers,
                    status: void 0 !== e.status ? e.status : this.status,
                    statusText: e.statusText || this.statusText,
                    url: e.url || this.url || void 0
                })
            }
        }
        class _a extends pd {
            constructor(e={}) {
                super(e),
                this.type = xe.Response,
                this.body = void 0 !== e.body ? e.body : null
            }
            clone(e={}) {
                return new _a({
                    body: void 0 !== e.body ? e.body : this.body,
                    headers: e.headers || this.headers,
                    status: void 0 !== e.status ? e.status : this.status,
                    statusText: e.statusText || this.statusText,
                    url: e.url || this.url || void 0
                })
            }
        }
        class mv extends pd {
            constructor(e) {
                super(e, 0, "Unknown Error"),
                this.name = "HttpErrorResponse",
                this.ok = !1,
                this.message = this.status >= 200 && this.status < 300 ? `Http failure during parsing for ${e.url || "(unknown url)"}` : `Http failure response for ${e.url || "(unknown url)"}: ${e.status} ${e.statusText}`,
                this.error = e.error || null
            }
        }
        function gd(n, e) {
            return {
                body: e,
                headers: n.headers,
                context: n.context,
                observe: n.observe,
                params: n.params,
                reportProgress: n.reportProgress,
                responseType: n.responseType,
                withCredentials: n.withCredentials
            }
        }
        let va = (()=>{
            class n {
                constructor(t) {
                    this.handler = t
                }
                request(t, r, i={}) {
                    let o;
                    if (t instanceof Ao)
                        o = t;
                    else {
                        let l, u;
                        l = i.headers instanceof xn ? i.headers : new xn(i.headers),
                        i.params && (u = i.params instanceof zn ? i.params : new zn({
                            fromObject: i.params
                        })),
                        o = new Ao(t,r,void 0 !== i.body ? i.body : null,{
                            headers: l,
                            context: i.context,
                            params: u,
                            reportProgress: i.reportProgress,
                            responseType: i.responseType || "json",
                            withCredentials: i.withCredentials
                        })
                    }
                    const s = br(o).pipe(function fN(n, e) {
                        return X(e) ? xi(n, e, 1) : xi(n, 1)
                    }(l=>this.handler.handle(l)));
                    if (t instanceof Ao || "events" === i.observe)
                        return s;
                    const a = s.pipe(av(l=>l instanceof _a));
                    switch (i.observe || "body") {
                    case "body":
                        switch (o.responseType) {
                        case "arraybuffer":
                            return a.pipe(xt(l=>{
                                if (null !== l.body && !(l.body instanceof ArrayBuffer))
                                    throw new Error("Response is not an ArrayBuffer.");
                                return l.body
                            }
                            ));
                        case "blob":
                            return a.pipe(xt(l=>{
                                if (null !== l.body && !(l.body instanceof Blob))
                                    throw new Error("Response is not a Blob.");
                                return l.body
                            }
                            ));
                        case "text":
                            return a.pipe(xt(l=>{
                                if (null !== l.body && "string" != typeof l.body)
                                    throw new Error("Response is not a string.");
                                return l.body
                            }
                            ));
                        default:
                            return a.pipe(xt(l=>l.body))
                        }
                    case "response":
                        return a;
                    default:
                        throw new Error(`Unreachable: unhandled observe type ${i.observe}}`)
                    }
                }
                delete(t, r={}) {
                    return this.request("DELETE", t, r)
                }
                get(t, r={}) {
                    return this.request("GET", t, r)
                }
                head(t, r={}) {
                    return this.request("HEAD", t, r)
                }
                jsonp(t, r) {
                    return this.request("JSONP", t, {
                        params: (new zn).append(r, "JSONP_CALLBACK"),
                        observe: "body",
                        responseType: "json"
                    })
                }
                options(t, r={}) {
                    return this.request("OPTIONS", t, r)
                }
                patch(t, r, i={}) {
                    return this.request("PATCH", t, gd(i, r))
                }
                post(t, r, i={}) {
                    return this.request("POST", t, gd(i, r))
                }
                put(t, r, i={}) {
                    return this.request("PUT", t, gd(i, r))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(lv))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        class gv {
            constructor(e, t) {
                this.next = e,
                this.interceptor = t
            }
            handle(e) {
                return this.interceptor.intercept(e, this.next)
            }
        }
        const yv = new S("HTTP_INTERCEPTORS");
        let bN = (()=>{
            class n {
                intercept(t, r) {
                    return r.handle(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        const DN = /^\)\]\}',?\n/;
        let _v = (()=>{
            class n {
                constructor(t) {
                    this.xhrFactory = t
                }
                handle(t) {
                    if ("JSONP" === t.method)
                        throw new Error("Attempted to construct Jsonp request without HttpClientJsonpModule installed.");
                    return new Fe(r=>{
                        const i = this.xhrFactory.build();
                        if (i.open(t.method, t.urlWithParams),
                        t.withCredentials && (i.withCredentials = !0),
                        t.headers.forEach((h,p)=>i.setRequestHeader(h, p.join(","))),
                        t.headers.has("Accept") || i.setRequestHeader("Accept", "application/json, text/plain, */*"),
                        !t.headers.has("Content-Type")) {
                            const h = t.detectContentTypeHeader();
                            null !== h && i.setRequestHeader("Content-Type", h)
                        }
                        if (t.responseType) {
                            const h = t.responseType.toLowerCase();
                            i.responseType = "json" !== h ? h : "text"
                        }
                        const o = t.serializeBody();
                        let s = null;
                        const a = ()=>{
                            if (null !== s)
                                return s;
                            const h = i.statusText || "OK"
                              , p = new xn(i.getAllResponseHeaders())
                              , m = function CN(n) {
                                return "responseURL"in n && n.responseURL ? n.responseURL : /^X-Request-URL:/m.test(n.getAllResponseHeaders()) ? n.getResponseHeader("X-Request-URL") : null
                            }(i) || t.url;
                            return s = new md({
                                headers: p,
                                status: i.status,
                                statusText: h,
                                url: m
                            }),
                            s
                        }
                          , l = ()=>{
                            let {headers: h, status: p, statusText: m, url: y} = a()
                              , _ = null;
                            204 !== p && (_ = void 0 === i.response ? i.responseText : i.response),
                            0 === p && (p = _ ? 200 : 0);
                            let g = p >= 200 && p < 300;
                            if ("json" === t.responseType && "string" == typeof _) {
                                const D = _;
                                _ = _.replace(DN, "");
                                try {
                                    _ = "" !== _ ? JSON.parse(_) : null
                                } catch (I) {
                                    _ = D,
                                    g && (g = !1,
                                    _ = {
                                        error: I,
                                        text: _
                                    })
                                }
                            }
                            g ? (r.next(new _a({
                                body: _,
                                headers: h,
                                status: p,
                                statusText: m,
                                url: y || void 0
                            })),
                            r.complete()) : r.error(new mv({
                                error: _,
                                headers: h,
                                status: p,
                                statusText: m,
                                url: y || void 0
                            }))
                        }
                          , u = h=>{
                            const {url: p} = a()
                              , m = new mv({
                                error: h,
                                status: i.status || 0,
                                statusText: i.statusText || "Unknown Error",
                                url: p || void 0
                            });
                            r.error(m)
                        }
                        ;
                        let c = !1;
                        const d = h=>{
                            c || (r.next(a()),
                            c = !0);
                            let p = {
                                type: xe.DownloadProgress,
                                loaded: h.loaded
                            };
                            h.lengthComputable && (p.total = h.total),
                            "text" === t.responseType && !!i.responseText && (p.partialText = i.responseText),
                            r.next(p)
                        }
                          , f = h=>{
                            let p = {
                                type: xe.UploadProgress,
                                loaded: h.loaded
                            };
                            h.lengthComputable && (p.total = h.total),
                            r.next(p)
                        }
                        ;
                        return i.addEventListener("load", l),
                        i.addEventListener("error", u),
                        i.addEventListener("timeout", u),
                        i.addEventListener("abort", u),
                        t.reportProgress && (i.addEventListener("progress", d),
                        null !== o && i.upload && i.upload.addEventListener("progress", f)),
                        i.send(o),
                        r.next({
                            type: xe.Sent
                        }),
                        ()=>{
                            i.removeEventListener("error", u),
                            i.removeEventListener("abort", u),
                            i.removeEventListener("load", l),
                            i.removeEventListener("timeout", u),
                            t.reportProgress && (i.removeEventListener("progress", d),
                            null !== o && i.upload && i.upload.removeEventListener("progress", f)),
                            i.readyState !== i.DONE && i.abort()
                        }
                    }
                    )
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(q_))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        const yd = new S("XSRF_COOKIE_NAME")
          , _d = new S("XSRF_HEADER_NAME");
        class vv {
        }
        let EN = (()=>{
            class n {
                constructor(t, r, i) {
                    this.doc = t,
                    this.platform = r,
                    this.cookieName = i,
                    this.lastCookieString = "",
                    this.lastToken = null,
                    this.parseCount = 0
                }
                getToken() {
                    if ("server" === this.platform)
                        return null;
                    const t = this.doc.cookie || "";
                    return t !== this.lastCookieString && (this.parseCount++,
                    this.lastToken = R_(t, this.cookieName),
                    this.lastCookieString = t),
                    this.lastToken
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(ge),w(Xs),w(yd))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )()
          , vd = (()=>{
            class n {
                constructor(t, r) {
                    this.tokenService = t,
                    this.headerName = r
                }
                intercept(t, r) {
                    const i = t.url.toLowerCase();
                    if ("GET" === t.method || "HEAD" === t.method || i.startsWith("http://") || i.startsWith("https://"))
                        return r.handle(t);
                    const o = this.tokenService.getToken();
                    return null !== o && !t.headers.has(this.headerName) && (t = t.clone({
                        headers: t.headers.set(this.headerName, o)
                    })),
                    r.handle(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(vv),w(_d))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )()
          , wN = (()=>{
            class n {
                constructor(t, r) {
                    this.backend = t,
                    this.injector = r,
                    this.chain = null
                }
                handle(t) {
                    if (null === this.chain) {
                        const r = this.injector.get(yv, []);
                        this.chain = r.reduceRight((i,o)=>new gv(i,o), this.backend)
                    }
                    return this.chain.handle(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(uv),w(vt))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )()
          , MN = (()=>{
            class n {
                static disable() {
                    return {
                        ngModule: n,
                        providers: [{
                            provide: vd,
                            useClass: bN
                        }]
                    }
                }
                static withOptions(t={}) {
                    return {
                        ngModule: n,
                        providers: [t.cookieName ? {
                            provide: yd,
                            useValue: t.cookieName
                        } : [], t.headerName ? {
                            provide: _d,
                            useValue: t.headerName
                        } : []]
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                providers: [vd, {
                    provide: yv,
                    useExisting: vd,
                    multi: !0
                }, {
                    provide: vv,
                    useClass: EN
                }, {
                    provide: yd,
                    useValue: "XSRF-TOKEN"
                }, {
                    provide: _d,
                    useValue: "X-XSRF-TOKEN"
                }]
            }),
            n
        }
        )()
          , AN = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                providers: [va, {
                    provide: lv,
                    useClass: wN
                }, _v, {
                    provide: uv,
                    useExisting: _v
                }],
                imports: [[MN.withOptions({
                    cookieName: "XSRF-TOKEN",
                    headerName: "X-XSRF-TOKEN"
                })]]
            }),
            n
        }
        )();
        const {isArray: TN} = Array
          , {getPrototypeOf: IN, prototype: SN, keys: xN} = Object;
        const {isArray: ON} = Array;
        function bv(n) {
            return xt(e=>function kN(n, e) {
                return ON(e) ? n(...e) : n(e)
            }(n, e))
        }
        function RN(n, e) {
            return n.reduce((t,r,i)=>(t[r] = e[i],
            t), {})
        }
        function Dv(...n) {
            const e = function IC(n) {
                return X(ml(n)) ? n.pop() : void 0
            }(n)
              , {args: t, keys: r} = function FN(n) {
                if (1 === n.length) {
                    const e = n[0];
                    if (TN(e))
                        return {
                            args: e,
                            keys: null
                        };
                    if (function NN(n) {
                        return n && "object" == typeof n && IN(n) === SN
                    }(e)) {
                        const t = xN(e);
                        return {
                            args: t.map(r=>e[r]),
                            keys: t
                        }
                    }
                }
                return {
                    args: n,
                    keys: null
                }
            }(n)
              , i = new Fe(o=>{
                const {length: s} = t;
                if (!s)
                    return void o.complete();
                const a = new Array(s);
                let l = s
                  , u = s;
                for (let c = 0; c < s; c++) {
                    let d = !1;
                    rn(t[c]).subscribe(St(o, f=>{
                        d || (d = !0,
                        u--),
                        a[c] = f
                    }
                    , ()=>l--, void 0, ()=>{
                        (!l || !d) && (u || o.next(r ? RN(r, a) : a),
                        o.complete())
                    }
                    ))
                }
            }
            );
            return e ? i.pipe(bv(e)) : i
        }
        let Cv = (()=>{
            class n {
                constructor(t, r) {
                    this._renderer = t,
                    this._elementRef = r,
                    this.onChange = i=>{}
                    ,
                    this.onTouched = ()=>{}
                }
                setProperty(t, r) {
                    this._renderer.setProperty(this._elementRef.nativeElement, t, r)
                }
                registerOnTouched(t) {
                    this.onTouched = t
                }
                registerOnChange(t) {
                    this.onChange = t
                }
                setDisabledState(t) {
                    this.setProperty("disabled", t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(gr),v(Pe))
            }
            ,
            n.\u0275dir = x({
                type: n
            }),
            n
        }
        )()
          , Dr = (()=>{
            class n extends Cv {
            }
            return n.\u0275fac = function() {
                let e;
                return function(r) {
                    return (e || (e = function ze(n) {
                        return Pn(()=>{
                            const e = n.prototype.constructor
                              , t = e[Cn] || Zl(e)
                              , r = Object.prototype;
                            let i = Object.getPrototypeOf(n.prototype).constructor;
                            for (; i && i !== r; ) {
                                const o = i[Cn] || Zl(i);
                                if (o && o !== t)
                                    return o;
                                i = Object.getPrototypeOf(i)
                            }
                            return o=>new o
                        }
                        )
                    }(n)))(r || n)
                }
            }(),
            n.\u0275dir = x({
                type: n,
                features: [Y]
            }),
            n
        }
        )();
        const _n = new S("NgValueAccessor")
          , LN = {
            provide: _n,
            useExisting: oe(()=>ba),
            multi: !0
        }
          , BN = new S("CompositionEventMode");
        let ba = (()=>{
            class n extends Cv {
                constructor(t, r, i) {
                    super(t, r),
                    this._compositionMode = i,
                    this._composing = !1,
                    null == this._compositionMode && (this._compositionMode = !function VN() {
                        const n = vr() ? vr().getUserAgent() : "";
                        return /android (\d+)/.test(n.toLowerCase())
                    }())
                }
                writeValue(t) {
                    this.setProperty("value", null == t ? "" : t)
                }
                _handleInput(t) {
                    (!this._compositionMode || this._compositionMode && !this._composing) && this.onChange(t)
                }
                _compositionStart() {
                    this._composing = !0
                }
                _compositionEnd(t) {
                    this._composing = !1,
                    this._compositionMode && this.onChange(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(gr),v(Pe),v(BN, 8))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["input", "formControlName", "", 3, "type", "checkbox"], ["textarea", "formControlName", ""], ["input", "formControl", "", 3, "type", "checkbox"], ["textarea", "formControl", ""], ["input", "ngModel", "", 3, "type", "checkbox"], ["textarea", "ngModel", ""], ["", "ngDefaultControl", ""]],
                hostBindings: function(t, r) {
                    1 & t && Ke("input", function(o) {
                        return r._handleInput(o.target.value)
                    })("blur", function() {
                        return r.onTouched()
                    })("compositionstart", function() {
                        return r._compositionStart()
                    })("compositionend", function(o) {
                        return r._compositionEnd(o.target.value)
                    })
                },
                features: [ae([LN]), Y]
            }),
            n
        }
        )();
        function qn(n) {
            return null == n || 0 === n.length
        }
        function wv(n) {
            return null != n && "number" == typeof n.length
        }
        const Qe = new S("NgValidators")
          , Wn = new S("NgAsyncValidators")
          , jN = /^(?=.{1,254}$)(?=.{1,64}@)[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/;
        class bd {
            static min(e) {
                return function Mv(n) {
                    return e=>{
                        if (qn(e.value) || qn(n))
                            return null;
                        const t = parseFloat(e.value);
                        return !isNaN(t) && t < n ? {
                            min: {
                                min: n,
                                actual: e.value
                            }
                        } : null
                    }
                }(e)
            }
            static max(e) {
                return function Av(n) {
                    return e=>{
                        if (qn(e.value) || qn(n))
                            return null;
                        const t = parseFloat(e.value);
                        return !isNaN(t) && t > n ? {
                            max: {
                                max: n,
                                actual: e.value
                            }
                        } : null
                    }
                }(e)
            }
            static required(e) {
                return function Tv(n) {
                    return qn(n.value) ? {
                        required: !0
                    } : null
                }(e)
            }
            static requiredTrue(e) {
                return function Iv(n) {
                    return !0 === n.value ? null : {
                        required: !0
                    }
                }(e)
            }
            static email(e) {
                return function Sv(n) {
                    return qn(n.value) || jN.test(n.value) ? null : {
                        email: !0
                    }
                }(e)
            }
            static minLength(e) {
                return function xv(n) {
                    return e=>qn(e.value) || !wv(e.value) ? null : e.value.length < n ? {
                        minlength: {
                            requiredLength: n,
                            actualLength: e.value.length
                        }
                    } : null
                }(e)
            }
            static maxLength(e) {
                return function Fv(n) {
                    return e=>wv(e.value) && e.value.length > n ? {
                        maxlength: {
                            requiredLength: n,
                            actualLength: e.value.length
                        }
                    } : null
                }(e)
            }
            static pattern(e) {
                return function Nv(n) {
                    if (!n)
                        return Da;
                    let e, t;
                    return "string" == typeof n ? (t = "",
                    "^" !== n.charAt(0) && (t += "^"),
                    t += n,
                    "$" !== n.charAt(n.length - 1) && (t += "$"),
                    e = new RegExp(t)) : (t = n.toString(),
                    e = n),
                    r=>{
                        if (qn(r.value))
                            return null;
                        const i = r.value;
                        return e.test(i) ? null : {
                            pattern: {
                                requiredPattern: t,
                                actualValue: i
                            }
                        }
                    }
                }(e)
            }
            static nullValidator(e) {
                return null
            }
            static compose(e) {
                return Vv(e)
            }
            static composeAsync(e) {
                return Bv(e)
            }
        }
        function Da(n) {
            return null
        }
        function Ov(n) {
            return null != n
        }
        function kv(n) {
            const e = Bs(n) ? Fi(n) : n;
            return ng(e),
            e
        }
        function Rv(n) {
            let e = {};
            return n.forEach(t=>{
                e = null != t ? Object.assign(Object.assign({}, e), t) : e
            }
            ),
            0 === Object.keys(e).length ? null : e
        }
        function Pv(n, e) {
            return e.map(t=>t(n))
        }
        function Lv(n) {
            return n.map(e=>function HN(n) {
                return !n.validate
            }(e) ? e : t=>e.validate(t))
        }
        function Vv(n) {
            if (!n)
                return null;
            const e = n.filter(Ov);
            return 0 == e.length ? null : function(t) {
                return Rv(Pv(t, e))
            }
        }
        function Dd(n) {
            return null != n ? Vv(Lv(n)) : null
        }
        function Bv(n) {
            if (!n)
                return null;
            const e = n.filter(Ov);
            return 0 == e.length ? null : function(t) {
                return Dv(Pv(t, e).map(kv)).pipe(xt(Rv))
            }
        }
        function Cd(n) {
            return null != n ? Bv(Lv(n)) : null
        }
        function jv(n, e) {
            return null === n ? [e] : Array.isArray(n) ? [...n, e] : [n, e]
        }
        function Hv(n) {
            return n._rawValidators
        }
        function Uv(n) {
            return n._rawAsyncValidators
        }
        function Ed(n) {
            return n ? Array.isArray(n) ? n : [n] : []
        }
        function Ca(n, e) {
            return Array.isArray(n) ? n.includes(e) : n === e
        }
        function $v(n, e) {
            const t = Ed(e);
            return Ed(n).forEach(i=>{
                Ca(t, i) || t.push(i)
            }
            ),
            t
        }
        function Gv(n, e) {
            return Ed(e).filter(t=>!Ca(n, t))
        }
        class zv {
            constructor() {
                this._rawValidators = [],
                this._rawAsyncValidators = [],
                this._onDestroyCallbacks = []
            }
            get value() {
                return this.control ? this.control.value : null
            }
            get valid() {
                return this.control ? this.control.valid : null
            }
            get invalid() {
                return this.control ? this.control.invalid : null
            }
            get pending() {
                return this.control ? this.control.pending : null
            }
            get disabled() {
                return this.control ? this.control.disabled : null
            }
            get enabled() {
                return this.control ? this.control.enabled : null
            }
            get errors() {
                return this.control ? this.control.errors : null
            }
            get pristine() {
                return this.control ? this.control.pristine : null
            }
            get dirty() {
                return this.control ? this.control.dirty : null
            }
            get touched() {
                return this.control ? this.control.touched : null
            }
            get status() {
                return this.control ? this.control.status : null
            }
            get untouched() {
                return this.control ? this.control.untouched : null
            }
            get statusChanges() {
                return this.control ? this.control.statusChanges : null
            }
            get valueChanges() {
                return this.control ? this.control.valueChanges : null
            }
            get path() {
                return null
            }
            _setValidators(e) {
                this._rawValidators = e || [],
                this._composedValidatorFn = Dd(this._rawValidators)
            }
            _setAsyncValidators(e) {
                this._rawAsyncValidators = e || [],
                this._composedAsyncValidatorFn = Cd(this._rawAsyncValidators)
            }
            get validator() {
                return this._composedValidatorFn || null
            }
            get asyncValidator() {
                return this._composedAsyncValidatorFn || null
            }
            _registerOnDestroy(e) {
                this._onDestroyCallbacks.push(e)
            }
            _invokeOnDestroyCallbacks() {
                this._onDestroyCallbacks.forEach(e=>e()),
                this._onDestroyCallbacks = []
            }
            reset(e) {
                this.control && this.control.reset(e)
            }
            hasError(e, t) {
                return !!this.control && this.control.hasError(e, t)
            }
            getError(e, t) {
                return this.control ? this.control.getError(e, t) : null
            }
        }
        class Fn extends zv {
            constructor() {
                super(...arguments),
                this._parent = null,
                this.name = null,
                this.valueAccessor = null
            }
        }
        class it extends zv {
            get formDirective() {
                return null
            }
            get path() {
                return null
            }
        }
        class qv {
            constructor(e) {
                this._cd = e
            }
            is(e) {
                var t, r, i;
                return "submitted" === e ? !!(null === (t = this._cd) || void 0 === t ? void 0 : t.submitted) : !!(null === (i = null === (r = this._cd) || void 0 === r ? void 0 : r.control) || void 0 === i ? void 0 : i[e])
            }
        }
        let Wv = (()=>{
            class n extends qv {
                constructor(t) {
                    super(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Fn, 2))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "formControlName", ""], ["", "ngModel", ""], ["", "formControl", ""]],
                hostVars: 14,
                hostBindings: function(t, r) {
                    2 & t && Je("ng-untouched", r.is("untouched"))("ng-touched", r.is("touched"))("ng-pristine", r.is("pristine"))("ng-dirty", r.is("dirty"))("ng-valid", r.is("valid"))("ng-invalid", r.is("invalid"))("ng-pending", r.is("pending"))
                },
                features: [Y]
            }),
            n
        }
        )()
          , Kv = (()=>{
            class n extends qv {
                constructor(t) {
                    super(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(it, 10))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "formGroupName", ""], ["", "formArrayName", ""], ["", "ngModelGroup", ""], ["", "formGroup", ""], ["form", 3, "ngNoForm", ""], ["", "ngForm", ""]],
                hostVars: 16,
                hostBindings: function(t, r) {
                    2 & t && Je("ng-untouched", r.is("untouched"))("ng-touched", r.is("touched"))("ng-pristine", r.is("pristine"))("ng-dirty", r.is("dirty"))("ng-valid", r.is("valid"))("ng-invalid", r.is("invalid"))("ng-pending", r.is("pending"))("ng-submitted", r.is("submitted"))
                },
                features: [Y]
            }),
            n
        }
        )();
        function To(n, e) {
            Ad(n, e),
            e.valueAccessor.writeValue(n.value),
            function QN(n, e) {
                e.valueAccessor.registerOnChange(t=>{
                    n._pendingValue = t,
                    n._pendingChange = !0,
                    n._pendingDirty = !0,
                    "change" === n.updateOn && Zv(n, e)
                }
                )
            }(n, e),
            function YN(n, e) {
                const t = (r,i)=>{
                    e.valueAccessor.writeValue(r),
                    i && e.viewToModelUpdate(r)
                }
                ;
                n.registerOnChange(t),
                e._registerOnDestroy(()=>{
                    n._unregisterOnChange(t)
                }
                )
            }(n, e),
            function ZN(n, e) {
                e.valueAccessor.registerOnTouched(()=>{
                    n._pendingTouched = !0,
                    "blur" === n.updateOn && n._pendingChange && Zv(n, e),
                    "submit" !== n.updateOn && n.markAsTouched()
                }
                )
            }(n, e),
            function KN(n, e) {
                if (e.valueAccessor.setDisabledState) {
                    const t = r=>{
                        e.valueAccessor.setDisabledState(r)
                    }
                    ;
                    n.registerOnDisabledChange(t),
                    e._registerOnDestroy(()=>{
                        n._unregisterOnDisabledChange(t)
                    }
                    )
                }
            }(n, e)
        }
        function Ma(n, e, t=!0) {
            const r = ()=>{}
            ;
            e.valueAccessor && (e.valueAccessor.registerOnChange(r),
            e.valueAccessor.registerOnTouched(r)),
            Ta(n, e),
            n && (e._invokeOnDestroyCallbacks(),
            n._registerOnCollectionChange(()=>{}
            ))
        }
        function Aa(n, e) {
            n.forEach(t=>{
                t.registerOnValidatorChange && t.registerOnValidatorChange(e)
            }
            )
        }
        function Ad(n, e) {
            const t = Hv(n);
            null !== e.validator ? n.setValidators(jv(t, e.validator)) : "function" == typeof t && n.setValidators([t]);
            const r = Uv(n);
            null !== e.asyncValidator ? n.setAsyncValidators(jv(r, e.asyncValidator)) : "function" == typeof r && n.setAsyncValidators([r]);
            const i = ()=>n.updateValueAndValidity();
            Aa(e._rawValidators, i),
            Aa(e._rawAsyncValidators, i)
        }
        function Ta(n, e) {
            let t = !1;
            if (null !== n) {
                if (null !== e.validator) {
                    const i = Hv(n);
                    if (Array.isArray(i) && i.length > 0) {
                        const o = i.filter(s=>s !== e.validator);
                        o.length !== i.length && (t = !0,
                        n.setValidators(o))
                    }
                }
                if (null !== e.asyncValidator) {
                    const i = Uv(n);
                    if (Array.isArray(i) && i.length > 0) {
                        const o = i.filter(s=>s !== e.asyncValidator);
                        o.length !== i.length && (t = !0,
                        n.setAsyncValidators(o))
                    }
                }
            }
            const r = ()=>{}
            ;
            return Aa(e._rawValidators, r),
            Aa(e._rawAsyncValidators, r),
            t
        }
        function Zv(n, e) {
            n._pendingDirty && n.markAsDirty(),
            n.setValue(n._pendingValue, {
                emitModelToViewChange: !1
            }),
            e.viewToModelUpdate(n._pendingValue),
            n._pendingChange = !1
        }
        function Yv(n, e) {
            Ad(n, e)
        }
        function Jv(n, e) {
            n._syncPendingControls(),
            e.forEach(t=>{
                const r = t.control;
                "submit" === r.updateOn && r._pendingChange && (t.viewToModelUpdate(r._pendingValue),
                r._pendingChange = !1)
            }
            )
        }
        function Sd(n, e) {
            const t = n.indexOf(e);
            t > -1 && n.splice(t, 1)
        }
        const Io = "VALID"
          , Ia = "INVALID"
          , Di = "PENDING"
          , So = "DISABLED";
        function Fd(n) {
            return (Sa(n) ? n.validators : n) || null
        }
        function eb(n) {
            return Array.isArray(n) ? Dd(n) : n || null
        }
        function Nd(n, e) {
            return (Sa(e) ? e.asyncValidators : n) || null
        }
        function tb(n) {
            return Array.isArray(n) ? Cd(n) : n || null
        }
        function Sa(n) {
            return null != n && !Array.isArray(n) && "object" == typeof n
        }
        const nb = n=>n instanceof Rd
          , Od = n=>n instanceof xa;
        function rb(n) {
            return nb(n) ? n.value : n.getRawValue()
        }
        function ib(n, e) {
            const t = Od(n)
              , r = n.controls;
            if (!(t ? Object.keys(r) : r).length)
                throw new M(1e3,"");
            if (!r[e])
                throw new M(1001,"")
        }
        function ob(n, e) {
            Od(n),
            n._forEachChild((r,i)=>{
                if (void 0 === e[i])
                    throw new M(1002,"")
            }
            )
        }
        class kd {
            constructor(e, t) {
                this._pendingDirty = !1,
                this._hasOwnPendingAsyncValidator = !1,
                this._pendingTouched = !1,
                this._onCollectionChange = ()=>{}
                ,
                this._parent = null,
                this.pristine = !0,
                this.touched = !1,
                this._onDisabledChange = [],
                this._rawValidators = e,
                this._rawAsyncValidators = t,
                this._composedValidatorFn = eb(this._rawValidators),
                this._composedAsyncValidatorFn = tb(this._rawAsyncValidators)
            }
            get validator() {
                return this._composedValidatorFn
            }
            set validator(e) {
                this._rawValidators = this._composedValidatorFn = e
            }
            get asyncValidator() {
                return this._composedAsyncValidatorFn
            }
            set asyncValidator(e) {
                this._rawAsyncValidators = this._composedAsyncValidatorFn = e
            }
            get parent() {
                return this._parent
            }
            get valid() {
                return this.status === Io
            }
            get invalid() {
                return this.status === Ia
            }
            get pending() {
                return this.status == Di
            }
            get disabled() {
                return this.status === So
            }
            get enabled() {
                return this.status !== So
            }
            get dirty() {
                return !this.pristine
            }
            get untouched() {
                return !this.touched
            }
            get updateOn() {
                return this._updateOn ? this._updateOn : this.parent ? this.parent.updateOn : "change"
            }
            setValidators(e) {
                this._rawValidators = e,
                this._composedValidatorFn = eb(e)
            }
            setAsyncValidators(e) {
                this._rawAsyncValidators = e,
                this._composedAsyncValidatorFn = tb(e)
            }
            addValidators(e) {
                this.setValidators($v(e, this._rawValidators))
            }
            addAsyncValidators(e) {
                this.setAsyncValidators($v(e, this._rawAsyncValidators))
            }
            removeValidators(e) {
                this.setValidators(Gv(e, this._rawValidators))
            }
            removeAsyncValidators(e) {
                this.setAsyncValidators(Gv(e, this._rawAsyncValidators))
            }
            hasValidator(e) {
                return Ca(this._rawValidators, e)
            }
            hasAsyncValidator(e) {
                return Ca(this._rawAsyncValidators, e)
            }
            clearValidators() {
                this.validator = null
            }
            clearAsyncValidators() {
                this.asyncValidator = null
            }
            markAsTouched(e={}) {
                this.touched = !0,
                this._parent && !e.onlySelf && this._parent.markAsTouched(e)
            }
            markAllAsTouched() {
                this.markAsTouched({
                    onlySelf: !0
                }),
                this._forEachChild(e=>e.markAllAsTouched())
            }
            markAsUntouched(e={}) {
                this.touched = !1,
                this._pendingTouched = !1,
                this._forEachChild(t=>{
                    t.markAsUntouched({
                        onlySelf: !0
                    })
                }
                ),
                this._parent && !e.onlySelf && this._parent._updateTouched(e)
            }
            markAsDirty(e={}) {
                this.pristine = !1,
                this._parent && !e.onlySelf && this._parent.markAsDirty(e)
            }
            markAsPristine(e={}) {
                this.pristine = !0,
                this._pendingDirty = !1,
                this._forEachChild(t=>{
                    t.markAsPristine({
                        onlySelf: !0
                    })
                }
                ),
                this._parent && !e.onlySelf && this._parent._updatePristine(e)
            }
            markAsPending(e={}) {
                this.status = Di,
                !1 !== e.emitEvent && this.statusChanges.emit(this.status),
                this._parent && !e.onlySelf && this._parent.markAsPending(e)
            }
            disable(e={}) {
                const t = this._parentMarkedDirty(e.onlySelf);
                this.status = So,
                this.errors = null,
                this._forEachChild(r=>{
                    r.disable(Object.assign(Object.assign({}, e), {
                        onlySelf: !0
                    }))
                }
                ),
                this._updateValue(),
                !1 !== e.emitEvent && (this.valueChanges.emit(this.value),
                this.statusChanges.emit(this.status)),
                this._updateAncestors(Object.assign(Object.assign({}, e), {
                    skipPristineCheck: t
                })),
                this._onDisabledChange.forEach(r=>r(!0))
            }
            enable(e={}) {
                const t = this._parentMarkedDirty(e.onlySelf);
                this.status = Io,
                this._forEachChild(r=>{
                    r.enable(Object.assign(Object.assign({}, e), {
                        onlySelf: !0
                    }))
                }
                ),
                this.updateValueAndValidity({
                    onlySelf: !0,
                    emitEvent: e.emitEvent
                }),
                this._updateAncestors(Object.assign(Object.assign({}, e), {
                    skipPristineCheck: t
                })),
                this._onDisabledChange.forEach(r=>r(!1))
            }
            _updateAncestors(e) {
                this._parent && !e.onlySelf && (this._parent.updateValueAndValidity(e),
                e.skipPristineCheck || this._parent._updatePristine(),
                this._parent._updateTouched())
            }
            setParent(e) {
                this._parent = e
            }
            updateValueAndValidity(e={}) {
                this._setInitialStatus(),
                this._updateValue(),
                this.enabled && (this._cancelExistingSubscription(),
                this.errors = this._runValidator(),
                this.status = this._calculateStatus(),
                (this.status === Io || this.status === Di) && this._runAsyncValidator(e.emitEvent)),
                !1 !== e.emitEvent && (this.valueChanges.emit(this.value),
                this.statusChanges.emit(this.status)),
                this._parent && !e.onlySelf && this._parent.updateValueAndValidity(e)
            }
            _updateTreeValidity(e={
                emitEvent: !0
            }) {
                this._forEachChild(t=>t._updateTreeValidity(e)),
                this.updateValueAndValidity({
                    onlySelf: !0,
                    emitEvent: e.emitEvent
                })
            }
            _setInitialStatus() {
                this.status = this._allControlsDisabled() ? So : Io
            }
            _runValidator() {
                return this.validator ? this.validator(this) : null
            }
            _runAsyncValidator(e) {
                if (this.asyncValidator) {
                    this.status = Di,
                    this._hasOwnPendingAsyncValidator = !0;
                    const t = kv(this.asyncValidator(this));
                    this._asyncValidationSubscription = t.subscribe(r=>{
                        this._hasOwnPendingAsyncValidator = !1,
                        this.setErrors(r, {
                            emitEvent: e
                        })
                    }
                    )
                }
            }
            _cancelExistingSubscription() {
                this._asyncValidationSubscription && (this._asyncValidationSubscription.unsubscribe(),
                this._hasOwnPendingAsyncValidator = !1)
            }
            setErrors(e, t={}) {
                this.errors = e,
                this._updateControlsErrors(!1 !== t.emitEvent)
            }
            get(e) {
                return function t1(n, e, t) {
                    if (null == e || (Array.isArray(e) || (e = e.split(t)),
                    Array.isArray(e) && 0 === e.length))
                        return null;
                    let r = n;
                    return e.forEach(i=>{
                        r = Od(r) ? r.controls.hasOwnProperty(i) ? r.controls[i] : null : (n=>n instanceof r1)(r) && r.at(i) || null
                    }
                    ),
                    r
                }(this, e, ".")
            }
            getError(e, t) {
                const r = t ? this.get(t) : this;
                return r && r.errors ? r.errors[e] : null
            }
            hasError(e, t) {
                return !!this.getError(e, t)
            }
            get root() {
                let e = this;
                for (; e._parent; )
                    e = e._parent;
                return e
            }
            _updateControlsErrors(e) {
                this.status = this._calculateStatus(),
                e && this.statusChanges.emit(this.status),
                this._parent && this._parent._updateControlsErrors(e)
            }
            _initObservables() {
                this.valueChanges = new je,
                this.statusChanges = new je
            }
            _calculateStatus() {
                return this._allControlsDisabled() ? So : this.errors ? Ia : this._hasOwnPendingAsyncValidator || this._anyControlsHaveStatus(Di) ? Di : this._anyControlsHaveStatus(Ia) ? Ia : Io
            }
            _anyControlsHaveStatus(e) {
                return this._anyControls(t=>t.status === e)
            }
            _anyControlsDirty() {
                return this._anyControls(e=>e.dirty)
            }
            _anyControlsTouched() {
                return this._anyControls(e=>e.touched)
            }
            _updatePristine(e={}) {
                this.pristine = !this._anyControlsDirty(),
                this._parent && !e.onlySelf && this._parent._updatePristine(e)
            }
            _updateTouched(e={}) {
                this.touched = this._anyControlsTouched(),
                this._parent && !e.onlySelf && this._parent._updateTouched(e)
            }
            _isBoxedValue(e) {
                return "object" == typeof e && null !== e && 2 === Object.keys(e).length && "value"in e && "disabled"in e
            }
            _registerOnCollectionChange(e) {
                this._onCollectionChange = e
            }
            _setUpdateStrategy(e) {
                Sa(e) && null != e.updateOn && (this._updateOn = e.updateOn)
            }
            _parentMarkedDirty(e) {
                return !e && !(!this._parent || !this._parent.dirty) && !this._parent._anyControlsDirty()
            }
        }
        class Rd extends kd {
            constructor(e=null, t, r) {
                super(Fd(t), Nd(r, t)),
                this.defaultValue = null,
                this._onChange = [],
                this._pendingChange = !1,
                this._applyFormState(e),
                this._setUpdateStrategy(t),
                this._initObservables(),
                this.updateValueAndValidity({
                    onlySelf: !0,
                    emitEvent: !!this.asyncValidator
                }),
                Sa(t) && t.initialValueIsDefault && (this.defaultValue = this._isBoxedValue(e) ? e.value : e)
            }
            setValue(e, t={}) {
                this.value = this._pendingValue = e,
                this._onChange.length && !1 !== t.emitModelToViewChange && this._onChange.forEach(r=>r(this.value, !1 !== t.emitViewToModelChange)),
                this.updateValueAndValidity(t)
            }
            patchValue(e, t={}) {
                this.setValue(e, t)
            }
            reset(e=this.defaultValue, t={}) {
                this._applyFormState(e),
                this.markAsPristine(t),
                this.markAsUntouched(t),
                this.setValue(this.value, t),
                this._pendingChange = !1
            }
            _updateValue() {}
            _anyControls(e) {
                return !1
            }
            _allControlsDisabled() {
                return this.disabled
            }
            registerOnChange(e) {
                this._onChange.push(e)
            }
            _unregisterOnChange(e) {
                Sd(this._onChange, e)
            }
            registerOnDisabledChange(e) {
                this._onDisabledChange.push(e)
            }
            _unregisterOnDisabledChange(e) {
                Sd(this._onDisabledChange, e)
            }
            _forEachChild(e) {}
            _syncPendingControls() {
                return !("submit" !== this.updateOn || (this._pendingDirty && this.markAsDirty(),
                this._pendingTouched && this.markAsTouched(),
                !this._pendingChange) || (this.setValue(this._pendingValue, {
                    onlySelf: !0,
                    emitModelToViewChange: !1
                }),
                0))
            }
            _applyFormState(e) {
                this._isBoxedValue(e) ? (this.value = this._pendingValue = e.value,
                e.disabled ? this.disable({
                    onlySelf: !0,
                    emitEvent: !1
                }) : this.enable({
                    onlySelf: !0,
                    emitEvent: !1
                })) : this.value = this._pendingValue = e
            }
        }
        class xa extends kd {
            constructor(e, t, r) {
                super(Fd(t), Nd(r, t)),
                this.controls = e,
                this._initObservables(),
                this._setUpdateStrategy(t),
                this._setUpControls(),
                this.updateValueAndValidity({
                    onlySelf: !0,
                    emitEvent: !!this.asyncValidator
                })
            }
            registerControl(e, t) {
                return this.controls[e] ? this.controls[e] : (this.controls[e] = t,
                t.setParent(this),
                t._registerOnCollectionChange(this._onCollectionChange),
                t)
            }
            addControl(e, t, r={}) {
                this.registerControl(e, t),
                this.updateValueAndValidity({
                    emitEvent: r.emitEvent
                }),
                this._onCollectionChange()
            }
            removeControl(e, t={}) {
                this.controls[e] && this.controls[e]._registerOnCollectionChange(()=>{}
                ),
                delete this.controls[e],
                this.updateValueAndValidity({
                    emitEvent: t.emitEvent
                }),
                this._onCollectionChange()
            }
            setControl(e, t, r={}) {
                this.controls[e] && this.controls[e]._registerOnCollectionChange(()=>{}
                ),
                delete this.controls[e],
                t && this.registerControl(e, t),
                this.updateValueAndValidity({
                    emitEvent: r.emitEvent
                }),
                this._onCollectionChange()
            }
            contains(e) {
                return this.controls.hasOwnProperty(e) && this.controls[e].enabled
            }
            setValue(e, t={}) {
                ob(this, e),
                Object.keys(e).forEach(r=>{
                    ib(this, r),
                    this.controls[r].setValue(e[r], {
                        onlySelf: !0,
                        emitEvent: t.emitEvent
                    })
                }
                ),
                this.updateValueAndValidity(t)
            }
            patchValue(e, t={}) {
                null != e && (Object.keys(e).forEach(r=>{
                    this.controls[r] && this.controls[r].patchValue(e[r], {
                        onlySelf: !0,
                        emitEvent: t.emitEvent
                    })
                }
                ),
                this.updateValueAndValidity(t))
            }
            reset(e={}, t={}) {
                this._forEachChild((r,i)=>{
                    r.reset(e[i], {
                        onlySelf: !0,
                        emitEvent: t.emitEvent
                    })
                }
                ),
                this._updatePristine(t),
                this._updateTouched(t),
                this.updateValueAndValidity(t)
            }
            getRawValue() {
                return this._reduceChildren({}, (e,t,r)=>(e[r] = rb(t),
                e))
            }
            _syncPendingControls() {
                let e = this._reduceChildren(!1, (t,r)=>!!r._syncPendingControls() || t);
                return e && this.updateValueAndValidity({
                    onlySelf: !0
                }),
                e
            }
            _forEachChild(e) {
                Object.keys(this.controls).forEach(t=>{
                    const r = this.controls[t];
                    r && e(r, t)
                }
                )
            }
            _setUpControls() {
                this._forEachChild(e=>{
                    e.setParent(this),
                    e._registerOnCollectionChange(this._onCollectionChange)
                }
                )
            }
            _updateValue() {
                this.value = this._reduceValue()
            }
            _anyControls(e) {
                for (const t of Object.keys(this.controls)) {
                    const r = this.controls[t];
                    if (this.contains(t) && e(r))
                        return !0
                }
                return !1
            }
            _reduceValue() {
                return this._reduceChildren({}, (e,t,r)=>((t.enabled || this.disabled) && (e[r] = t.value),
                e))
            }
            _reduceChildren(e, t) {
                let r = e;
                return this._forEachChild((i,o)=>{
                    r = t(r, i, o)
                }
                ),
                r
            }
            _allControlsDisabled() {
                for (const e of Object.keys(this.controls))
                    if (this.controls[e].enabled)
                        return !1;
                return Object.keys(this.controls).length > 0 || this.disabled
            }
        }
        class r1 extends kd {
            constructor(e, t, r) {
                super(Fd(t), Nd(r, t)),
                this.controls = e,
                this._initObservables(),
                this._setUpdateStrategy(t),
                this._setUpControls(),
                this.updateValueAndValidity({
                    onlySelf: !0,
                    emitEvent: !!this.asyncValidator
                })
            }
            at(e) {
                return this.controls[e]
            }
            push(e, t={}) {
                this.controls.push(e),
                this._registerControl(e),
                this.updateValueAndValidity({
                    emitEvent: t.emitEvent
                }),
                this._onCollectionChange()
            }
            insert(e, t, r={}) {
                this.controls.splice(e, 0, t),
                this._registerControl(t),
                this.updateValueAndValidity({
                    emitEvent: r.emitEvent
                })
            }
            removeAt(e, t={}) {
                this.controls[e] && this.controls[e]._registerOnCollectionChange(()=>{}
                ),
                this.controls.splice(e, 1),
                this.updateValueAndValidity({
                    emitEvent: t.emitEvent
                })
            }
            setControl(e, t, r={}) {
                this.controls[e] && this.controls[e]._registerOnCollectionChange(()=>{}
                ),
                this.controls.splice(e, 1),
                t && (this.controls.splice(e, 0, t),
                this._registerControl(t)),
                this.updateValueAndValidity({
                    emitEvent: r.emitEvent
                }),
                this._onCollectionChange()
            }
            get length() {
                return this.controls.length
            }
            setValue(e, t={}) {
                ob(this, e),
                e.forEach((r,i)=>{
                    ib(this, i),
                    this.at(i).setValue(r, {
                        onlySelf: !0,
                        emitEvent: t.emitEvent
                    })
                }
                ),
                this.updateValueAndValidity(t)
            }
            patchValue(e, t={}) {
                null != e && (e.forEach((r,i)=>{
                    this.at(i) && this.at(i).patchValue(r, {
                        onlySelf: !0,
                        emitEvent: t.emitEvent
                    })
                }
                ),
                this.updateValueAndValidity(t))
            }
            reset(e=[], t={}) {
                this._forEachChild((r,i)=>{
                    r.reset(e[i], {
                        onlySelf: !0,
                        emitEvent: t.emitEvent
                    })
                }
                ),
                this._updatePristine(t),
                this._updateTouched(t),
                this.updateValueAndValidity(t)
            }
            getRawValue() {
                return this.controls.map(e=>rb(e))
            }
            clear(e={}) {
                this.controls.length < 1 || (this._forEachChild(t=>t._registerOnCollectionChange(()=>{}
                )),
                this.controls.splice(0),
                this.updateValueAndValidity({
                    emitEvent: e.emitEvent
                }))
            }
            _syncPendingControls() {
                let e = this.controls.reduce((t,r)=>!!r._syncPendingControls() || t, !1);
                return e && this.updateValueAndValidity({
                    onlySelf: !0
                }),
                e
            }
            _forEachChild(e) {
                this.controls.forEach((t,r)=>{
                    e(t, r)
                }
                )
            }
            _updateValue() {
                this.value = this.controls.filter(e=>e.enabled || this.disabled).map(e=>e.value)
            }
            _anyControls(e) {
                return this.controls.some(t=>t.enabled && e(t))
            }
            _setUpControls() {
                this._forEachChild(e=>this._registerControl(e))
            }
            _allControlsDisabled() {
                for (const e of this.controls)
                    if (e.enabled)
                        return !1;
                return this.controls.length > 0 || this.disabled
            }
            _registerControl(e) {
                e.setParent(this),
                e._registerOnCollectionChange(this._onCollectionChange)
            }
        }
        const o1 = {
            provide: it,
            useExisting: oe(()=>Fa)
        }
          , xo = (()=>Promise.resolve(null))();
        let Fa = (()=>{
            class n extends it {
                constructor(t, r) {
                    super(),
                    this.submitted = !1,
                    this._directives = new Set,
                    this.ngSubmit = new je,
                    this.form = new xa({},Dd(t),Cd(r))
                }
                ngAfterViewInit() {
                    this._setUpdateStrategy()
                }
                get formDirective() {
                    return this
                }
                get control() {
                    return this.form
                }
                get path() {
                    return []
                }
                get controls() {
                    return this.form.controls
                }
                addControl(t) {
                    xo.then(()=>{
                        const r = this._findContainer(t.path);
                        t.control = r.registerControl(t.name, t.control),
                        To(t.control, t),
                        t.control.updateValueAndValidity({
                            emitEvent: !1
                        }),
                        this._directives.add(t)
                    }
                    )
                }
                getControl(t) {
                    return this.form.get(t.path)
                }
                removeControl(t) {
                    xo.then(()=>{
                        const r = this._findContainer(t.path);
                        r && r.removeControl(t.name),
                        this._directives.delete(t)
                    }
                    )
                }
                addFormGroup(t) {
                    xo.then(()=>{
                        const r = this._findContainer(t.path)
                          , i = new xa({});
                        Yv(i, t),
                        r.registerControl(t.name, i),
                        i.updateValueAndValidity({
                            emitEvent: !1
                        })
                    }
                    )
                }
                removeFormGroup(t) {
                    xo.then(()=>{
                        const r = this._findContainer(t.path);
                        r && r.removeControl(t.name)
                    }
                    )
                }
                getFormGroup(t) {
                    return this.form.get(t.path)
                }
                updateModel(t, r) {
                    xo.then(()=>{
                        this.form.get(t.path).setValue(r)
                    }
                    )
                }
                setValue(t) {
                    this.control.setValue(t)
                }
                onSubmit(t) {
                    return this.submitted = !0,
                    Jv(this.form, this._directives),
                    this.ngSubmit.emit(t),
                    !1
                }
                onReset() {
                    this.resetForm()
                }
                resetForm(t) {
                    this.form.reset(t),
                    this.submitted = !1
                }
                _setUpdateStrategy() {
                    this.options && null != this.options.updateOn && (this.form._updateOn = this.options.updateOn)
                }
                _findContainer(t) {
                    return t.pop(),
                    t.length ? this.form.get(t) : this.form
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Qe, 10),v(Wn, 10))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["form", 3, "ngNoForm", "", 3, "formGroup", ""], ["ng-form"], ["", "ngForm", ""]],
                hostBindings: function(t, r) {
                    1 & t && Ke("submit", function(o) {
                        return r.onSubmit(o)
                    })("reset", function() {
                        return r.onReset()
                    })
                },
                inputs: {
                    options: ["ngFormOptions", "options"]
                },
                outputs: {
                    ngSubmit: "ngSubmit"
                },
                exportAs: ["ngForm"],
                features: [ae([o1]), Y]
            }),
            n
        }
        )()
          , cb = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["form", 3, "ngNoForm", "", 3, "ngNativeValidate", ""]],
                hostAttrs: ["novalidate", ""]
            }),
            n
        }
        )()
          , fb = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({}),
            n
        }
        )();
        const Pd = new S("NgModelWithFormControlWarning")
          , h1 = {
            provide: it,
            useExisting: oe(()=>Fo)
        };
        let Fo = (()=>{
            class n extends it {
                constructor(t, r) {
                    super(),
                    this.validators = t,
                    this.asyncValidators = r,
                    this.submitted = !1,
                    this._onCollectionChange = ()=>this._updateDomValue(),
                    this.directives = [],
                    this.form = null,
                    this.ngSubmit = new je,
                    this._setValidators(t),
                    this._setAsyncValidators(r)
                }
                ngOnChanges(t) {
                    this._checkFormPresent(),
                    t.hasOwnProperty("form") && (this._updateValidators(),
                    this._updateDomValue(),
                    this._updateRegistrations(),
                    this._oldForm = this.form)
                }
                ngOnDestroy() {
                    this.form && (Ta(this.form, this),
                    this.form._onCollectionChange === this._onCollectionChange && this.form._registerOnCollectionChange(()=>{}
                    ))
                }
                get formDirective() {
                    return this
                }
                get control() {
                    return this.form
                }
                get path() {
                    return []
                }
                addControl(t) {
                    const r = this.form.get(t.path);
                    return To(r, t),
                    r.updateValueAndValidity({
                        emitEvent: !1
                    }),
                    this.directives.push(t),
                    r
                }
                getControl(t) {
                    return this.form.get(t.path)
                }
                removeControl(t) {
                    Ma(t.control || null, t, !1),
                    Sd(this.directives, t)
                }
                addFormGroup(t) {
                    this._setUpFormContainer(t)
                }
                removeFormGroup(t) {
                    this._cleanUpFormContainer(t)
                }
                getFormGroup(t) {
                    return this.form.get(t.path)
                }
                addFormArray(t) {
                    this._setUpFormContainer(t)
                }
                removeFormArray(t) {
                    this._cleanUpFormContainer(t)
                }
                getFormArray(t) {
                    return this.form.get(t.path)
                }
                updateModel(t, r) {
                    this.form.get(t.path).setValue(r)
                }
                onSubmit(t) {
                    return this.submitted = !0,
                    Jv(this.form, this.directives),
                    this.ngSubmit.emit(t),
                    !1
                }
                onReset() {
                    this.resetForm()
                }
                resetForm(t) {
                    this.form.reset(t),
                    this.submitted = !1
                }
                _updateDomValue() {
                    this.directives.forEach(t=>{
                        const r = t.control
                          , i = this.form.get(t.path);
                        r !== i && (Ma(r || null, t),
                        nb(i) && (To(i, t),
                        t.control = i))
                    }
                    ),
                    this.form._updateTreeValidity({
                        emitEvent: !1
                    })
                }
                _setUpFormContainer(t) {
                    const r = this.form.get(t.path);
                    Yv(r, t),
                    r.updateValueAndValidity({
                        emitEvent: !1
                    })
                }
                _cleanUpFormContainer(t) {
                    if (this.form) {
                        const r = this.form.get(t.path);
                        r && function XN(n, e) {
                            return Ta(n, e)
                        }(r, t) && r.updateValueAndValidity({
                            emitEvent: !1
                        })
                    }
                }
                _updateRegistrations() {
                    this.form._registerOnCollectionChange(this._onCollectionChange),
                    this._oldForm && this._oldForm._registerOnCollectionChange(()=>{}
                    )
                }
                _updateValidators() {
                    Ad(this.form, this),
                    this._oldForm && Ta(this._oldForm, this)
                }
                _checkFormPresent() {}
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Qe, 10),v(Wn, 10))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "formGroup", ""]],
                hostBindings: function(t, r) {
                    1 & t && Ke("submit", function(o) {
                        return r.onSubmit(o)
                    })("reset", function() {
                        return r.onReset()
                    })
                },
                inputs: {
                    form: ["formGroup", "form"]
                },
                outputs: {
                    ngSubmit: "ngSubmit"
                },
                exportAs: ["ngForm"],
                features: [ae([h1]), Y, sn]
            }),
            n
        }
        )();
        const g1 = {
            provide: Fn,
            useExisting: oe(()=>Bd)
        };
        let Bd = (()=>{
            class n extends Fn {
                constructor(t, r, i, o, s) {
                    super(),
                    this._ngModelWarningConfig = s,
                    this._added = !1,
                    this.update = new je,
                    this._ngModelWarningSent = !1,
                    this._parent = t,
                    this._setValidators(r),
                    this._setAsyncValidators(i),
                    this.valueAccessor = function Id(n, e) {
                        if (!e)
                            return null;
                        let t, r, i;
                        return Array.isArray(e),
                        e.forEach(o=>{
                            o.constructor === ba ? t = o : function e1(n) {
                                return Object.getPrototypeOf(n.constructor) === Dr
                            }(o) ? r = o : i = o
                        }
                        ),
                        i || r || t || null
                    }(0, o)
                }
                set isDisabled(t) {}
                ngOnChanges(t) {
                    this._added || this._setUpControl(),
                    function Td(n, e) {
                        if (!n.hasOwnProperty("model"))
                            return !1;
                        const t = n.model;
                        return !!t.isFirstChange() || !Object.is(e, t.currentValue)
                    }(t, this.viewModel) && (this.viewModel = this.model,
                    this.formDirective.updateModel(this, this.model))
                }
                ngOnDestroy() {
                    this.formDirective && this.formDirective.removeControl(this)
                }
                viewToModelUpdate(t) {
                    this.viewModel = t,
                    this.update.emit(t)
                }
                get path() {
                    return function wa(n, e) {
                        return [...e.path, n]
                    }(null == this.name ? this.name : this.name.toString(), this._parent)
                }
                get formDirective() {
                    return this._parent ? this._parent.formDirective : null
                }
                _checkParentType() {}
                _setUpControl() {
                    this._checkParentType(),
                    this.control = this.formDirective.addControl(this),
                    this.control.disabled && this.valueAccessor.setDisabledState && this.valueAccessor.setDisabledState(!0),
                    this._added = !0
                }
            }
            return n._ngModelWarningSentOnce = !1,
            n.\u0275fac = function(t) {
                return new (t || n)(v(it, 13),v(Qe, 10),v(Wn, 10),v(_n, 10),v(Pd, 8))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "formControlName", ""]],
                inputs: {
                    name: ["formControlName", "name"],
                    isDisabled: ["disabled", "isDisabled"],
                    model: ["ngModel", "model"]
                },
                outputs: {
                    update: "ngModelChange"
                },
                features: [ae([g1]), Y, sn]
            }),
            n
        }
        )()
          , Ib = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[fb]]
            }),
            n
        }
        )()
          , N1 = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [Ib]
            }),
            n
        }
        )()
          , O1 = (()=>{
            class n {
                static withConfig(t) {
                    return {
                        ngModule: n,
                        providers: [{
                            provide: Pd,
                            useValue: t.warnOnNgModelWithFormControl
                        }]
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [Ib]
            }),
            n
        }
        )();
        class Sb {
        }
        const Nn = "*";
        function R1(n, e) {
            return {
                type: 7,
                name: n,
                definitions: e,
                options: {}
            }
        }
        function P1(n, e=null) {
            return {
                type: 4,
                styles: e,
                timings: n
            }
        }
        function xb(n, e=null) {
            return {
                type: 2,
                steps: n,
                options: e
            }
        }
        function Na(n) {
            return {
                type: 6,
                styles: n,
                offset: null
            }
        }
        function L1(n, e, t) {
            return {
                type: 0,
                name: n,
                styles: e,
                options: t
            }
        }
        function V1(n, e, t=null) {
            return {
                type: 1,
                expr: n,
                animation: e,
                options: t
            }
        }
        function Fb(n) {
            Promise.resolve(null).then(n)
        }
        class No {
            constructor(e=0, t=0) {
                this._onDoneFns = [],
                this._onStartFns = [],
                this._onDestroyFns = [],
                this._started = !1,
                this._destroyed = !1,
                this._finished = !1,
                this._position = 0,
                this.parentPlayer = null,
                this.totalTime = e + t
            }
            _onFinish() {
                this._finished || (this._finished = !0,
                this._onDoneFns.forEach(e=>e()),
                this._onDoneFns = [])
            }
            onStart(e) {
                this._onStartFns.push(e)
            }
            onDone(e) {
                this._onDoneFns.push(e)
            }
            onDestroy(e) {
                this._onDestroyFns.push(e)
            }
            hasStarted() {
                return this._started
            }
            init() {}
            play() {
                this.hasStarted() || (this._onStart(),
                this.triggerMicrotask()),
                this._started = !0
            }
            triggerMicrotask() {
                Fb(()=>this._onFinish())
            }
            _onStart() {
                this._onStartFns.forEach(e=>e()),
                this._onStartFns = []
            }
            pause() {}
            restart() {}
            finish() {
                this._onFinish()
            }
            destroy() {
                this._destroyed || (this._destroyed = !0,
                this.hasStarted() || this._onStart(),
                this.finish(),
                this._onDestroyFns.forEach(e=>e()),
                this._onDestroyFns = [])
            }
            reset() {
                this._started = !1
            }
            setPosition(e) {
                this._position = this.totalTime ? e * this.totalTime : 1
            }
            getPosition() {
                return this.totalTime ? this._position / this.totalTime : 1
            }
            triggerCallback(e) {
                const t = "start" == e ? this._onStartFns : this._onDoneFns;
                t.forEach(r=>r()),
                t.length = 0
            }
        }
        class Nb {
            constructor(e) {
                this._onDoneFns = [],
                this._onStartFns = [],
                this._finished = !1,
                this._started = !1,
                this._destroyed = !1,
                this._onDestroyFns = [],
                this.parentPlayer = null,
                this.totalTime = 0,
                this.players = e;
                let t = 0
                  , r = 0
                  , i = 0;
                const o = this.players.length;
                0 == o ? Fb(()=>this._onFinish()) : this.players.forEach(s=>{
                    s.onDone(()=>{
                        ++t == o && this._onFinish()
                    }
                    ),
                    s.onDestroy(()=>{
                        ++r == o && this._onDestroy()
                    }
                    ),
                    s.onStart(()=>{
                        ++i == o && this._onStart()
                    }
                    )
                }
                ),
                this.totalTime = this.players.reduce((s,a)=>Math.max(s, a.totalTime), 0)
            }
            _onFinish() {
                this._finished || (this._finished = !0,
                this._onDoneFns.forEach(e=>e()),
                this._onDoneFns = [])
            }
            init() {
                this.players.forEach(e=>e.init())
            }
            onStart(e) {
                this._onStartFns.push(e)
            }
            _onStart() {
                this.hasStarted() || (this._started = !0,
                this._onStartFns.forEach(e=>e()),
                this._onStartFns = [])
            }
            onDone(e) {
                this._onDoneFns.push(e)
            }
            onDestroy(e) {
                this._onDestroyFns.push(e)
            }
            hasStarted() {
                return this._started
            }
            play() {
                this.parentPlayer || this.init(),
                this._onStart(),
                this.players.forEach(e=>e.play())
            }
            pause() {
                this.players.forEach(e=>e.pause())
            }
            restart() {
                this.players.forEach(e=>e.restart())
            }
            finish() {
                this._onFinish(),
                this.players.forEach(e=>e.finish())
            }
            destroy() {
                this._onDestroy()
            }
            _onDestroy() {
                this._destroyed || (this._destroyed = !0,
                this._onFinish(),
                this.players.forEach(e=>e.destroy()),
                this._onDestroyFns.forEach(e=>e()),
                this._onDestroyFns = [])
            }
            reset() {
                this.players.forEach(e=>e.reset()),
                this._destroyed = !1,
                this._finished = !1,
                this._started = !1
            }
            setPosition(e) {
                const t = e * this.totalTime;
                this.players.forEach(r=>{
                    const i = r.totalTime ? Math.min(1, t / r.totalTime) : 1;
                    r.setPosition(i)
                }
                )
            }
            getPosition() {
                const e = this.players.reduce((t,r)=>null === t || r.totalTime > t.totalTime ? r : t, null);
                return null != e ? e.getPosition() : 0
            }
            beforeDestroy() {
                this.players.forEach(e=>{
                    e.beforeDestroy && e.beforeDestroy()
                }
                )
            }
            triggerCallback(e) {
                const t = "start" == e ? this._onStartFns : this._onDoneFns;
                t.forEach(r=>r()),
                t.length = 0
            }
        }
        const K = !1;
        function Ob(n) {
            return new M(3e3,K)
        }
        function _O() {
            return "undefined" != typeof window && void 0 !== window.document
        }
        function Gd() {
            return "undefined" != typeof process && "[object process]" === {}.toString.call(process)
        }
        function Kn(n) {
            switch (n.length) {
            case 0:
                return new No;
            case 1:
                return n[0];
            default:
                return new Nb(n)
            }
        }
        function kb(n, e, t, r, i={}, o={}) {
            const s = []
              , a = [];
            let l = -1
              , u = null;
            if (r.forEach(c=>{
                const d = c.offset
                  , f = d == l
                  , h = f && u || {};
                Object.keys(c).forEach(p=>{
                    let m = p
                      , y = c[p];
                    if ("offset" !== p)
                        switch (m = e.normalizePropertyName(m, s),
                        y) {
                        case "!":
                            y = i[p];
                            break;
                        case Nn:
                            y = o[p];
                            break;
                        default:
                            y = e.normalizeStyleValue(p, m, y, s)
                        }
                    h[m] = y
                }
                ),
                f || a.push(h),
                u = h,
                l = d
            }
            ),
            s.length)
                throw function aO(n) {
                    return new M(3502,K)
                }();
            return a
        }
        function zd(n, e, t, r) {
            switch (e) {
            case "start":
                n.onStart(()=>r(t && qd(t, "start", n)));
                break;
            case "done":
                n.onDone(()=>r(t && qd(t, "done", n)));
                break;
            case "destroy":
                n.onDestroy(()=>r(t && qd(t, "destroy", n)))
            }
        }
        function qd(n, e, t) {
            const r = t.totalTime
              , o = Wd(n.element, n.triggerName, n.fromState, n.toState, e || n.phaseName, null == r ? n.totalTime : r, !!t.disabled)
              , s = n._data;
            return null != s && (o._data = s),
            o
        }
        function Wd(n, e, t, r, i="", o=0, s) {
            return {
                element: n,
                triggerName: e,
                fromState: t,
                toState: r,
                phaseName: i,
                totalTime: o,
                disabled: !!s
            }
        }
        function Dt(n, e, t) {
            let r;
            return n instanceof Map ? (r = n.get(e),
            r || n.set(e, r = t)) : (r = n[e],
            r || (r = n[e] = t)),
            r
        }
        function Rb(n) {
            const e = n.indexOf(":");
            return [n.substring(1, e), n.substr(e + 1)]
        }
        let Kd = (n,e)=>!1
          , Pb = (n,e,t)=>[]
          , Lb = null;
        function Qd(n) {
            const e = n.parentNode || n.host;
            return e === Lb ? null : e
        }
        (Gd() || "undefined" != typeof Element) && (_O() ? (Lb = (()=>document.documentElement)(),
        Kd = (n,e)=>{
            for (; e; ) {
                if (e === n)
                    return !0;
                e = Qd(e)
            }
            return !1
        }
        ) : Kd = (n,e)=>n.contains(e),
        Pb = (n,e,t)=>{
            if (t)
                return Array.from(n.querySelectorAll(e));
            const r = n.querySelector(e);
            return r ? [r] : []
        }
        );
        let Er = null
          , Vb = !1;
        function Bb(n) {
            Er || (Er = function bO() {
                return "undefined" != typeof document ? document.body : null
            }() || {},
            Vb = !!Er.style && "WebkitAppearance"in Er.style);
            let e = !0;
            return Er.style && !function vO(n) {
                return "ebkit" == n.substring(1, 6)
            }(n) && (e = n in Er.style,
            !e && Vb && (e = "Webkit" + n.charAt(0).toUpperCase() + n.substr(1)in Er.style)),
            e
        }
        const jb = Kd
          , Hb = Pb;
        let Ub = (()=>{
            class n {
                validateStyleProperty(t) {
                    return Bb(t)
                }
                matchesElement(t, r) {
                    return !1
                }
                containsElement(t, r) {
                    return jb(t, r)
                }
                getParentElement(t) {
                    return Qd(t)
                }
                query(t, r, i) {
                    return Hb(t, r, i)
                }
                computeStyle(t, r, i) {
                    return i || ""
                }
                animate(t, r, i, o, s, a=[], l) {
                    return new No(i,o)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )()
          , Zd = (()=>{
            class n {
            }
            return n.NOOP = new Ub,
            n
        }
        )();
        const Yd = "ng-enter"
          , ka = "ng-leave"
          , Ra = "ng-trigger"
          , Pa = ".ng-trigger"
          , Gb = "ng-animating"
          , Xd = ".ng-animating";
        function wr(n) {
            if ("number" == typeof n)
                return n;
            const e = n.match(/^(-?[\.\d]+)(m?s)/);
            return !e || e.length < 2 ? 0 : Jd(parseFloat(e[1]), e[2])
        }
        function Jd(n, e) {
            return "s" === e ? 1e3 * n : n
        }
        function La(n, e, t) {
            return n.hasOwnProperty("duration") ? n : function EO(n, e, t) {
                let i, o = 0, s = "";
                if ("string" == typeof n) {
                    const a = n.match(/^(-?[\.\d]+)(m?s)(?:\s+(-?[\.\d]+)(m?s))?(?:\s+([-a-z]+(?:\(.+?\))?))?$/i);
                    if (null === a)
                        return e.push(Ob()),
                        {
                            duration: 0,
                            delay: 0,
                            easing: ""
                        };
                    i = Jd(parseFloat(a[1]), a[2]);
                    const l = a[3];
                    null != l && (o = Jd(parseFloat(l), a[4]));
                    const u = a[5];
                    u && (s = u)
                } else
                    i = n;
                if (!t) {
                    let a = !1
                      , l = e.length;
                    i < 0 && (e.push(function B1() {
                        return new M(3100,K)
                    }()),
                    a = !0),
                    o < 0 && (e.push(function j1() {
                        return new M(3101,K)
                    }()),
                    a = !0),
                    a && e.splice(l, 0, Ob())
                }
                return {
                    duration: i,
                    delay: o,
                    easing: s
                }
            }(n, e, t)
        }
        function Ci(n, e={}) {
            return Object.keys(n).forEach(t=>{
                e[t] = n[t]
            }
            ),
            e
        }
        function Qn(n, e, t={}) {
            if (e)
                for (let r in n)
                    t[r] = n[r];
            else
                Ci(n, t);
            return t
        }
        function qb(n, e, t) {
            return t ? e + ":" + t + ";" : ""
        }
        function Wb(n) {
            let e = "";
            for (let t = 0; t < n.style.length; t++) {
                const r = n.style.item(t);
                e += qb(0, r, n.style.getPropertyValue(r))
            }
            for (const t in n.style)
                n.style.hasOwnProperty(t) && !t.startsWith("_") && (e += qb(0, AO(t), n.style[t]));
            n.setAttribute("style", e)
        }
        function vn(n, e, t) {
            n.style && (Object.keys(e).forEach(r=>{
                const i = tf(r);
                t && !t.hasOwnProperty(r) && (t[r] = n.style[i]),
                n.style[i] = e[r]
            }
            ),
            Gd() && Wb(n))
        }
        function Mr(n, e) {
            n.style && (Object.keys(e).forEach(t=>{
                const r = tf(t);
                n.style[r] = ""
            }
            ),
            Gd() && Wb(n))
        }
        function Oo(n) {
            return Array.isArray(n) ? 1 == n.length ? n[0] : xb(n) : n
        }
        const ef = new RegExp("{{\\s*(.+?)\\s*}}","g");
        function Kb(n) {
            let e = [];
            if ("string" == typeof n) {
                let t;
                for (; t = ef.exec(n); )
                    e.push(t[1]);
                ef.lastIndex = 0
            }
            return e
        }
        function Va(n, e, t) {
            const r = n.toString()
              , i = r.replace(ef, (o,s)=>{
                let a = e[s];
                return e.hasOwnProperty(s) || (t.push(function U1(n) {
                    return new M(3003,K)
                }()),
                a = ""),
                a.toString()
            }
            );
            return i == r ? n : i
        }
        function Ba(n) {
            const e = [];
            let t = n.next();
            for (; !t.done; )
                e.push(t.value),
                t = n.next();
            return e
        }
        const MO = /-+([a-z0-9])/g;
        function tf(n) {
            return n.replace(MO, (...e)=>e[1].toUpperCase())
        }
        function AO(n) {
            return n.replace(/([a-z])([A-Z])/g, "$1-$2").toLowerCase()
        }
        function Ct(n, e, t) {
            switch (e.type) {
            case 7:
                return n.visitTrigger(e, t);
            case 0:
                return n.visitState(e, t);
            case 1:
                return n.visitTransition(e, t);
            case 2:
                return n.visitSequence(e, t);
            case 3:
                return n.visitGroup(e, t);
            case 4:
                return n.visitAnimate(e, t);
            case 5:
                return n.visitKeyframes(e, t);
            case 6:
                return n.visitStyle(e, t);
            case 8:
                return n.visitReference(e, t);
            case 9:
                return n.visitAnimateChild(e, t);
            case 10:
                return n.visitAnimateRef(e, t);
            case 11:
                return n.visitQuery(e, t);
            case 12:
                return n.visitStagger(e, t);
            default:
                throw function $1(n) {
                    return new M(3004,K)
                }()
            }
        }
        function Qb(n, e) {
            return window.getComputedStyle(n)[e]
        }
        function NO(n, e) {
            const t = [];
            return "string" == typeof n ? n.split(/\s*,\s*/).forEach(r=>function OO(n, e, t) {
                if (":" == n[0]) {
                    const l = function kO(n, e) {
                        switch (n) {
                        case ":enter":
                            return "void => *";
                        case ":leave":
                            return "* => void";
                        case ":increment":
                            return (t,r)=>parseFloat(r) > parseFloat(t);
                        case ":decrement":
                            return (t,r)=>parseFloat(r) < parseFloat(t);
                        default:
                            return e.push(function rO(n) {
                                return new M(3016,K)
                            }()),
                            "* => *"
                        }
                    }(n, t);
                    if ("function" == typeof l)
                        return void e.push(l);
                    n = l
                }
                const r = n.match(/^(\*|[-\w]+)\s*(<?[=-]>)\s*(\*|[-\w]+)$/);
                if (null == r || r.length < 4)
                    return t.push(function nO(n) {
                        return new M(3015,K)
                    }()),
                    e;
                const i = r[1]
                  , o = r[2]
                  , s = r[3];
                e.push(Zb(i, s));
                "<" == o[0] && !("*" == i && "*" == s) && e.push(Zb(s, i))
            }(r, t, e)) : t.push(n),
            t
        }
        const $a = new Set(["true", "1"])
          , Ga = new Set(["false", "0"]);
        function Zb(n, e) {
            const t = $a.has(n) || Ga.has(n)
              , r = $a.has(e) || Ga.has(e);
            return (i,o)=>{
                let s = "*" == n || n == i
                  , a = "*" == e || e == o;
                return !s && t && "boolean" == typeof i && (s = i ? $a.has(n) : Ga.has(n)),
                !a && r && "boolean" == typeof o && (a = o ? $a.has(e) : Ga.has(e)),
                s && a
            }
        }
        const RO = new RegExp("s*:selfs*,?","g");
        function nf(n, e, t, r) {
            return new PO(n).build(e, t, r)
        }
        class PO {
            constructor(e) {
                this._driver = e
            }
            build(e, t, r) {
                const i = new BO(t);
                this._resetContextStyleTimingState(i);
                const o = Ct(this, Oo(e), i);
                return i.unsupportedCSSPropertiesFound.size && i.unsupportedCSSPropertiesFound.keys(),
                o
            }
            _resetContextStyleTimingState(e) {
                e.currentQuerySelector = "",
                e.collectedStyles = {},
                e.collectedStyles[""] = {},
                e.currentTime = 0
            }
            visitTrigger(e, t) {
                let r = t.queryCount = 0
                  , i = t.depCount = 0;
                const o = []
                  , s = [];
                return "@" == e.name.charAt(0) && t.errors.push(function z1() {
                    return new M(3006,K)
                }()),
                e.definitions.forEach(a=>{
                    if (this._resetContextStyleTimingState(t),
                    0 == a.type) {
                        const l = a
                          , u = l.name;
                        u.toString().split(/\s*,\s*/).forEach(c=>{
                            l.name = c,
                            o.push(this.visitState(l, t))
                        }
                        ),
                        l.name = u
                    } else if (1 == a.type) {
                        const l = this.visitTransition(a, t);
                        r += l.queryCount,
                        i += l.depCount,
                        s.push(l)
                    } else
                        t.errors.push(function q1() {
                            return new M(3007,K)
                        }())
                }
                ),
                {
                    type: 7,
                    name: e.name,
                    states: o,
                    transitions: s,
                    queryCount: r,
                    depCount: i,
                    options: null
                }
            }
            visitState(e, t) {
                const r = this.visitStyle(e.styles, t)
                  , i = e.options && e.options.params || null;
                if (r.containsDynamicStyles) {
                    const o = new Set
                      , s = i || {};
                    r.styles.forEach(a=>{
                        if (za(a)) {
                            const l = a;
                            Object.keys(l).forEach(u=>{
                                Kb(l[u]).forEach(c=>{
                                    s.hasOwnProperty(c) || o.add(c)
                                }
                                )
                            }
                            )
                        }
                    }
                    ),
                    o.size && (Ba(o.values()),
                    t.errors.push(function W1(n, e) {
                        return new M(3008,K)
                    }()))
                }
                return {
                    type: 0,
                    name: e.name,
                    style: r,
                    options: i ? {
                        params: i
                    } : null
                }
            }
            visitTransition(e, t) {
                t.queryCount = 0,
                t.depCount = 0;
                const r = Ct(this, Oo(e.animation), t);
                return {
                    type: 1,
                    matchers: NO(e.expr, t.errors),
                    animation: r,
                    queryCount: t.queryCount,
                    depCount: t.depCount,
                    options: Ar(e.options)
                }
            }
            visitSequence(e, t) {
                return {
                    type: 2,
                    steps: e.steps.map(r=>Ct(this, r, t)),
                    options: Ar(e.options)
                }
            }
            visitGroup(e, t) {
                const r = t.currentTime;
                let i = 0;
                const o = e.steps.map(s=>{
                    t.currentTime = r;
                    const a = Ct(this, s, t);
                    return i = Math.max(i, t.currentTime),
                    a
                }
                );
                return t.currentTime = i,
                {
                    type: 3,
                    steps: o,
                    options: Ar(e.options)
                }
            }
            visitAnimate(e, t) {
                const r = function HO(n, e) {
                    if (n.hasOwnProperty("duration"))
                        return n;
                    if ("number" == typeof n)
                        return rf(La(n, e).duration, 0, "");
                    const t = n;
                    if (t.split(/\s+/).some(o=>"{" == o.charAt(0) && "{" == o.charAt(1))) {
                        const o = rf(0, 0, "");
                        return o.dynamic = !0,
                        o.strValue = t,
                        o
                    }
                    const i = La(t, e);
                    return rf(i.duration, i.delay, i.easing)
                }(e.timings, t.errors);
                t.currentAnimateTimings = r;
                let i, o = e.styles ? e.styles : Na({});
                if (5 == o.type)
                    i = this.visitKeyframes(o, t);
                else {
                    let s = e.styles
                      , a = !1;
                    if (!s) {
                        a = !0;
                        const u = {};
                        r.easing && (u.easing = r.easing),
                        s = Na(u)
                    }
                    t.currentTime += r.duration + r.delay;
                    const l = this.visitStyle(s, t);
                    l.isEmptyStep = a,
                    i = l
                }
                return t.currentAnimateTimings = null,
                {
                    type: 4,
                    timings: r,
                    style: i,
                    options: null
                }
            }
            visitStyle(e, t) {
                const r = this._makeStyleAst(e, t);
                return this._validateStyleAst(r, t),
                r
            }
            _makeStyleAst(e, t) {
                const r = [];
                Array.isArray(e.styles) ? e.styles.forEach(s=>{
                    "string" == typeof s ? s == Nn ? r.push(s) : t.errors.push(function K1(n) {
                        return new M(3002,K)
                    }()) : r.push(s)
                }
                ) : r.push(e.styles);
                let i = !1
                  , o = null;
                return r.forEach(s=>{
                    if (za(s)) {
                        const a = s
                          , l = a.easing;
                        if (l && (o = l,
                        delete a.easing),
                        !i)
                            for (let u in a)
                                if (a[u].toString().indexOf("{{") >= 0) {
                                    i = !0;
                                    break
                                }
                    }
                }
                ),
                {
                    type: 6,
                    styles: r,
                    easing: o,
                    offset: e.offset,
                    containsDynamicStyles: i,
                    options: null
                }
            }
            _validateStyleAst(e, t) {
                const r = t.currentAnimateTimings;
                let i = t.currentTime
                  , o = t.currentTime;
                r && o > 0 && (o -= r.duration + r.delay),
                e.styles.forEach(s=>{
                    "string" != typeof s && Object.keys(s).forEach(a=>{
                        if (!this._driver.validateStyleProperty(a))
                            return delete s[a],
                            void t.unsupportedCSSPropertiesFound.add(a);
                        const l = t.collectedStyles[t.currentQuerySelector]
                          , u = l[a];
                        let c = !0;
                        u && (o != i && o >= u.startTime && i <= u.endTime && (t.errors.push(function Q1(n, e, t, r, i) {
                            return new M(3010,K)
                        }()),
                        c = !1),
                        o = u.startTime),
                        c && (l[a] = {
                            startTime: o,
                            endTime: i
                        }),
                        t.options && function wO(n, e, t) {
                            const r = e.params || {}
                              , i = Kb(n);
                            i.length && i.forEach(o=>{
                                r.hasOwnProperty(o) || t.push(function H1(n) {
                                    return new M(3001,K)
                                }())
                            }
                            )
                        }(s[a], t.options, t.errors)
                    }
                    )
                }
                )
            }
            visitKeyframes(e, t) {
                const r = {
                    type: 5,
                    styles: [],
                    options: null
                };
                if (!t.currentAnimateTimings)
                    return t.errors.push(function Z1() {
                        return new M(3011,K)
                    }()),
                    r;
                let o = 0;
                const s = [];
                let a = !1
                  , l = !1
                  , u = 0;
                const c = e.steps.map(_=>{
                    const g = this._makeStyleAst(_, t);
                    let D = null != g.offset ? g.offset : function jO(n) {
                        if ("string" == typeof n)
                            return null;
                        let e = null;
                        if (Array.isArray(n))
                            n.forEach(t=>{
                                if (za(t) && t.hasOwnProperty("offset")) {
                                    const r = t;
                                    e = parseFloat(r.offset),
                                    delete r.offset
                                }
                            }
                            );
                        else if (za(n) && n.hasOwnProperty("offset")) {
                            const t = n;
                            e = parseFloat(t.offset),
                            delete t.offset
                        }
                        return e
                    }(g.styles)
                      , I = 0;
                    return null != D && (o++,
                    I = g.offset = D),
                    l = l || I < 0 || I > 1,
                    a = a || I < u,
                    u = I,
                    s.push(I),
                    g
                }
                );
                l && t.errors.push(function Y1() {
                    return new M(3012,K)
                }()),
                a && t.errors.push(function X1() {
                    return new M(3200,K)
                }());
                const d = e.steps.length;
                let f = 0;
                o > 0 && o < d ? t.errors.push(function J1() {
                    return new M(3202,K)
                }()) : 0 == o && (f = 1 / (d - 1));
                const h = d - 1
                  , p = t.currentTime
                  , m = t.currentAnimateTimings
                  , y = m.duration;
                return c.forEach((_,g)=>{
                    const D = f > 0 ? g == h ? 1 : f * g : s[g]
                      , I = D * y;
                    t.currentTime = p + m.delay + I,
                    m.duration = I,
                    this._validateStyleAst(_, t),
                    _.offset = D,
                    r.styles.push(_)
                }
                ),
                r
            }
            visitReference(e, t) {
                return {
                    type: 8,
                    animation: Ct(this, Oo(e.animation), t),
                    options: Ar(e.options)
                }
            }
            visitAnimateChild(e, t) {
                return t.depCount++,
                {
                    type: 9,
                    options: Ar(e.options)
                }
            }
            visitAnimateRef(e, t) {
                return {
                    type: 10,
                    animation: this.visitReference(e.animation, t),
                    options: Ar(e.options)
                }
            }
            visitQuery(e, t) {
                const r = t.currentQuerySelector
                  , i = e.options || {};
                t.queryCount++,
                t.currentQuery = e;
                const [o,s] = function LO(n) {
                    const e = !!n.split(/\s*,\s*/).find(t=>":self" == t);
                    return e && (n = n.replace(RO, "")),
                    n = n.replace(/@\*/g, Pa).replace(/@\w+/g, t=>Pa + "-" + t.substr(1)).replace(/:animating/g, Xd),
                    [n, e]
                }(e.selector);
                t.currentQuerySelector = r.length ? r + " " + o : o,
                Dt(t.collectedStyles, t.currentQuerySelector, {});
                const a = Ct(this, Oo(e.animation), t);
                return t.currentQuery = null,
                t.currentQuerySelector = r,
                {
                    type: 11,
                    selector: o,
                    limit: i.limit || 0,
                    optional: !!i.optional,
                    includeSelf: s,
                    animation: a,
                    originalSelector: e.selector,
                    options: Ar(e.options)
                }
            }
            visitStagger(e, t) {
                t.currentQuery || t.errors.push(function eO() {
                    return new M(3013,K)
                }());
                const r = "full" === e.timings ? {
                    duration: 0,
                    delay: 0,
                    easing: "full"
                } : La(e.timings, t.errors, !0);
                return {
                    type: 12,
                    animation: Ct(this, Oo(e.animation), t),
                    timings: r,
                    options: null
                }
            }
        }
        class BO {
            constructor(e) {
                this.errors = e,
                this.queryCount = 0,
                this.depCount = 0,
                this.currentTransition = null,
                this.currentQuery = null,
                this.currentQuerySelector = null,
                this.currentAnimateTimings = null,
                this.currentTime = 0,
                this.collectedStyles = {},
                this.options = null,
                this.unsupportedCSSPropertiesFound = new Set
            }
        }
        function za(n) {
            return !Array.isArray(n) && "object" == typeof n
        }
        function Ar(n) {
            return n ? (n = Ci(n)).params && (n.params = function VO(n) {
                return n ? Ci(n) : null
            }(n.params)) : n = {},
            n
        }
        function rf(n, e, t) {
            return {
                duration: n,
                delay: e,
                easing: t
            }
        }
        function of(n, e, t, r, i, o, s=null, a=!1) {
            return {
                type: 1,
                element: n,
                keyframes: e,
                preStyleProps: t,
                postStyleProps: r,
                duration: i,
                delay: o,
                totalTime: i + o,
                easing: s,
                subTimeline: a
            }
        }
        class qa {
            constructor() {
                this._map = new Map
            }
            get(e) {
                return this._map.get(e) || []
            }
            append(e, t) {
                let r = this._map.get(e);
                r || this._map.set(e, r = []),
                r.push(...t)
            }
            has(e) {
                return this._map.has(e)
            }
            clear() {
                this._map.clear()
            }
        }
        const GO = new RegExp(":enter","g")
          , qO = new RegExp(":leave","g");
        function sf(n, e, t, r, i, o={}, s={}, a, l, u=[]) {
            return (new WO).buildKeyframes(n, e, t, r, i, o, s, a, l, u)
        }
        class WO {
            buildKeyframes(e, t, r, i, o, s, a, l, u, c=[]) {
                u = u || new qa;
                const d = new af(e,t,u,i,o,c,[]);
                d.options = l,
                d.currentTimeline.setStyles([s], null, d.errors, l),
                Ct(this, r, d);
                const f = d.timelines.filter(h=>h.containsAnimation());
                if (Object.keys(a).length) {
                    let h;
                    for (let p = f.length - 1; p >= 0; p--) {
                        const m = f[p];
                        if (m.element === t) {
                            h = m;
                            break
                        }
                    }
                    h && !h.allowOnlyTimelineStyles() && h.setStyles([a], null, d.errors, l)
                }
                return f.length ? f.map(h=>h.buildKeyframes()) : [of(t, [], [], [], 0, 0, "", !1)]
            }
            visitTrigger(e, t) {}
            visitState(e, t) {}
            visitTransition(e, t) {}
            visitAnimateChild(e, t) {
                const r = t.subInstructions.get(t.element);
                if (r) {
                    const i = t.createSubContext(e.options)
                      , o = t.currentTimeline.currentTime
                      , s = this._visitSubInstructions(r, i, i.options);
                    o != s && t.transformIntoNewTimeline(s)
                }
                t.previousNode = e
            }
            visitAnimateRef(e, t) {
                const r = t.createSubContext(e.options);
                r.transformIntoNewTimeline(),
                this.visitReference(e.animation, r),
                t.transformIntoNewTimeline(r.currentTimeline.currentTime),
                t.previousNode = e
            }
            _visitSubInstructions(e, t, r) {
                let o = t.currentTimeline.currentTime;
                const s = null != r.duration ? wr(r.duration) : null
                  , a = null != r.delay ? wr(r.delay) : null;
                return 0 !== s && e.forEach(l=>{
                    const u = t.appendInstructionToTimeline(l, s, a);
                    o = Math.max(o, u.duration + u.delay)
                }
                ),
                o
            }
            visitReference(e, t) {
                t.updateOptions(e.options, !0),
                Ct(this, e.animation, t),
                t.previousNode = e
            }
            visitSequence(e, t) {
                const r = t.subContextCount;
                let i = t;
                const o = e.options;
                if (o && (o.params || o.delay) && (i = t.createSubContext(o),
                i.transformIntoNewTimeline(),
                null != o.delay)) {
                    6 == i.previousNode.type && (i.currentTimeline.snapshotCurrentStyles(),
                    i.previousNode = Wa);
                    const s = wr(o.delay);
                    i.delayNextStep(s)
                }
                e.steps.length && (e.steps.forEach(s=>Ct(this, s, i)),
                i.currentTimeline.applyStylesToKeyframe(),
                i.subContextCount > r && i.transformIntoNewTimeline()),
                t.previousNode = e
            }
            visitGroup(e, t) {
                const r = [];
                let i = t.currentTimeline.currentTime;
                const o = e.options && e.options.delay ? wr(e.options.delay) : 0;
                e.steps.forEach(s=>{
                    const a = t.createSubContext(e.options);
                    o && a.delayNextStep(o),
                    Ct(this, s, a),
                    i = Math.max(i, a.currentTimeline.currentTime),
                    r.push(a.currentTimeline)
                }
                ),
                r.forEach(s=>t.currentTimeline.mergeTimelineCollectedStyles(s)),
                t.transformIntoNewTimeline(i),
                t.previousNode = e
            }
            _visitTiming(e, t) {
                if (e.dynamic) {
                    const r = e.strValue;
                    return La(t.params ? Va(r, t.params, t.errors) : r, t.errors)
                }
                return {
                    duration: e.duration,
                    delay: e.delay,
                    easing: e.easing
                }
            }
            visitAnimate(e, t) {
                const r = t.currentAnimateTimings = this._visitTiming(e.timings, t)
                  , i = t.currentTimeline;
                r.delay && (t.incrementTime(r.delay),
                i.snapshotCurrentStyles());
                const o = e.style;
                5 == o.type ? this.visitKeyframes(o, t) : (t.incrementTime(r.duration),
                this.visitStyle(o, t),
                i.applyStylesToKeyframe()),
                t.currentAnimateTimings = null,
                t.previousNode = e
            }
            visitStyle(e, t) {
                const r = t.currentTimeline
                  , i = t.currentAnimateTimings;
                !i && r.getCurrentStyleProperties().length && r.forwardFrame();
                const o = i && i.easing || e.easing;
                e.isEmptyStep ? r.applyEmptyStep(o) : r.setStyles(e.styles, o, t.errors, t.options),
                t.previousNode = e
            }
            visitKeyframes(e, t) {
                const r = t.currentAnimateTimings
                  , i = t.currentTimeline.duration
                  , o = r.duration
                  , a = t.createSubContext().currentTimeline;
                a.easing = r.easing,
                e.styles.forEach(l=>{
                    a.forwardTime((l.offset || 0) * o),
                    a.setStyles(l.styles, l.easing, t.errors, t.options),
                    a.applyStylesToKeyframe()
                }
                ),
                t.currentTimeline.mergeTimelineCollectedStyles(a),
                t.transformIntoNewTimeline(i + o),
                t.previousNode = e
            }
            visitQuery(e, t) {
                const r = t.currentTimeline.currentTime
                  , i = e.options || {}
                  , o = i.delay ? wr(i.delay) : 0;
                o && (6 === t.previousNode.type || 0 == r && t.currentTimeline.getCurrentStyleProperties().length) && (t.currentTimeline.snapshotCurrentStyles(),
                t.previousNode = Wa);
                let s = r;
                const a = t.invokeQuery(e.selector, e.originalSelector, e.limit, e.includeSelf, !!i.optional, t.errors);
                t.currentQueryTotal = a.length;
                let l = null;
                a.forEach((u,c)=>{
                    t.currentQueryIndex = c;
                    const d = t.createSubContext(e.options, u);
                    o && d.delayNextStep(o),
                    u === t.element && (l = d.currentTimeline),
                    Ct(this, e.animation, d),
                    d.currentTimeline.applyStylesToKeyframe(),
                    s = Math.max(s, d.currentTimeline.currentTime)
                }
                ),
                t.currentQueryIndex = 0,
                t.currentQueryTotal = 0,
                t.transformIntoNewTimeline(s),
                l && (t.currentTimeline.mergeTimelineCollectedStyles(l),
                t.currentTimeline.snapshotCurrentStyles()),
                t.previousNode = e
            }
            visitStagger(e, t) {
                const r = t.parentContext
                  , i = t.currentTimeline
                  , o = e.timings
                  , s = Math.abs(o.duration)
                  , a = s * (t.currentQueryTotal - 1);
                let l = s * t.currentQueryIndex;
                switch (o.duration < 0 ? "reverse" : o.easing) {
                case "reverse":
                    l = a - l;
                    break;
                case "full":
                    l = r.currentStaggerTime
                }
                const c = t.currentTimeline;
                l && c.delayNextStep(l);
                const d = c.currentTime;
                Ct(this, e.animation, t),
                t.previousNode = e,
                r.currentStaggerTime = i.currentTime - d + (i.startTime - r.currentTimeline.startTime)
            }
        }
        const Wa = {};
        class af {
            constructor(e, t, r, i, o, s, a, l) {
                this._driver = e,
                this.element = t,
                this.subInstructions = r,
                this._enterClassName = i,
                this._leaveClassName = o,
                this.errors = s,
                this.timelines = a,
                this.parentContext = null,
                this.currentAnimateTimings = null,
                this.previousNode = Wa,
                this.subContextCount = 0,
                this.options = {},
                this.currentQueryIndex = 0,
                this.currentQueryTotal = 0,
                this.currentStaggerTime = 0,
                this.currentTimeline = l || new Ka(this._driver,t,0),
                a.push(this.currentTimeline)
            }
            get params() {
                return this.options.params
            }
            updateOptions(e, t) {
                if (!e)
                    return;
                const r = e;
                let i = this.options;
                null != r.duration && (i.duration = wr(r.duration)),
                null != r.delay && (i.delay = wr(r.delay));
                const o = r.params;
                if (o) {
                    let s = i.params;
                    s || (s = this.options.params = {}),
                    Object.keys(o).forEach(a=>{
                        (!t || !s.hasOwnProperty(a)) && (s[a] = Va(o[a], s, this.errors))
                    }
                    )
                }
            }
            _copyOptions() {
                const e = {};
                if (this.options) {
                    const t = this.options.params;
                    if (t) {
                        const r = e.params = {};
                        Object.keys(t).forEach(i=>{
                            r[i] = t[i]
                        }
                        )
                    }
                }
                return e
            }
            createSubContext(e=null, t, r) {
                const i = t || this.element
                  , o = new af(this._driver,i,this.subInstructions,this._enterClassName,this._leaveClassName,this.errors,this.timelines,this.currentTimeline.fork(i, r || 0));
                return o.previousNode = this.previousNode,
                o.currentAnimateTimings = this.currentAnimateTimings,
                o.options = this._copyOptions(),
                o.updateOptions(e),
                o.currentQueryIndex = this.currentQueryIndex,
                o.currentQueryTotal = this.currentQueryTotal,
                o.parentContext = this,
                this.subContextCount++,
                o
            }
            transformIntoNewTimeline(e) {
                return this.previousNode = Wa,
                this.currentTimeline = this.currentTimeline.fork(this.element, e),
                this.timelines.push(this.currentTimeline),
                this.currentTimeline
            }
            appendInstructionToTimeline(e, t, r) {
                const i = {
                    duration: null != t ? t : e.duration,
                    delay: this.currentTimeline.currentTime + (null != r ? r : 0) + e.delay,
                    easing: ""
                }
                  , o = new KO(this._driver,e.element,e.keyframes,e.preStyleProps,e.postStyleProps,i,e.stretchStartingKeyframe);
                return this.timelines.push(o),
                i
            }
            incrementTime(e) {
                this.currentTimeline.forwardTime(this.currentTimeline.duration + e)
            }
            delayNextStep(e) {
                e > 0 && this.currentTimeline.delayNextStep(e)
            }
            invokeQuery(e, t, r, i, o, s) {
                let a = [];
                if (i && a.push(this.element),
                e.length > 0) {
                    e = (e = e.replace(GO, "." + this._enterClassName)).replace(qO, "." + this._leaveClassName);
                    let u = this._driver.query(this.element, e, 1 != r);
                    0 !== r && (u = r < 0 ? u.slice(u.length + r, u.length) : u.slice(0, r)),
                    a.push(...u)
                }
                return !o && 0 == a.length && s.push(function tO(n) {
                    return new M(3014,K)
                }()),
                a
            }
        }
        class Ka {
            constructor(e, t, r, i) {
                this._driver = e,
                this.element = t,
                this.startTime = r,
                this._elementTimelineStylesLookup = i,
                this.duration = 0,
                this._previousKeyframe = {},
                this._currentKeyframe = {},
                this._keyframes = new Map,
                this._styleSummary = {},
                this._pendingStyles = {},
                this._backFill = {},
                this._currentEmptyStepKeyframe = null,
                this._elementTimelineStylesLookup || (this._elementTimelineStylesLookup = new Map),
                this._localTimelineStyles = Object.create(this._backFill, {}),
                this._globalTimelineStyles = this._elementTimelineStylesLookup.get(t),
                this._globalTimelineStyles || (this._globalTimelineStyles = this._localTimelineStyles,
                this._elementTimelineStylesLookup.set(t, this._localTimelineStyles)),
                this._loadKeyframe()
            }
            containsAnimation() {
                switch (this._keyframes.size) {
                case 0:
                    return !1;
                case 1:
                    return this.getCurrentStyleProperties().length > 0;
                default:
                    return !0
                }
            }
            getCurrentStyleProperties() {
                return Object.keys(this._currentKeyframe)
            }
            get currentTime() {
                return this.startTime + this.duration
            }
            delayNextStep(e) {
                const t = 1 == this._keyframes.size && Object.keys(this._pendingStyles).length;
                this.duration || t ? (this.forwardTime(this.currentTime + e),
                t && this.snapshotCurrentStyles()) : this.startTime += e
            }
            fork(e, t) {
                return this.applyStylesToKeyframe(),
                new Ka(this._driver,e,t || this.currentTime,this._elementTimelineStylesLookup)
            }
            _loadKeyframe() {
                this._currentKeyframe && (this._previousKeyframe = this._currentKeyframe),
                this._currentKeyframe = this._keyframes.get(this.duration),
                this._currentKeyframe || (this._currentKeyframe = Object.create(this._backFill, {}),
                this._keyframes.set(this.duration, this._currentKeyframe))
            }
            forwardFrame() {
                this.duration += 1,
                this._loadKeyframe()
            }
            forwardTime(e) {
                this.applyStylesToKeyframe(),
                this.duration = e,
                this._loadKeyframe()
            }
            _updateStyle(e, t) {
                this._localTimelineStyles[e] = t,
                this._globalTimelineStyles[e] = t,
                this._styleSummary[e] = {
                    time: this.currentTime,
                    value: t
                }
            }
            allowOnlyTimelineStyles() {
                return this._currentEmptyStepKeyframe !== this._currentKeyframe
            }
            applyEmptyStep(e) {
                e && (this._previousKeyframe.easing = e),
                Object.keys(this._globalTimelineStyles).forEach(t=>{
                    this._backFill[t] = this._globalTimelineStyles[t] || Nn,
                    this._currentKeyframe[t] = Nn
                }
                ),
                this._currentEmptyStepKeyframe = this._currentKeyframe
            }
            setStyles(e, t, r, i) {
                t && (this._previousKeyframe.easing = t);
                const o = i && i.params || {}
                  , s = function QO(n, e) {
                    const t = {};
                    let r;
                    return n.forEach(i=>{
                        "*" === i ? (r = r || Object.keys(e),
                        r.forEach(o=>{
                            t[o] = Nn
                        }
                        )) : Qn(i, !1, t)
                    }
                    ),
                    t
                }(e, this._globalTimelineStyles);
                Object.keys(s).forEach(a=>{
                    const l = Va(s[a], o, r);
                    this._pendingStyles[a] = l,
                    this._localTimelineStyles.hasOwnProperty(a) || (this._backFill[a] = this._globalTimelineStyles.hasOwnProperty(a) ? this._globalTimelineStyles[a] : Nn),
                    this._updateStyle(a, l)
                }
                )
            }
            applyStylesToKeyframe() {
                const e = this._pendingStyles
                  , t = Object.keys(e);
                0 != t.length && (this._pendingStyles = {},
                t.forEach(r=>{
                    this._currentKeyframe[r] = e[r]
                }
                ),
                Object.keys(this._localTimelineStyles).forEach(r=>{
                    this._currentKeyframe.hasOwnProperty(r) || (this._currentKeyframe[r] = this._localTimelineStyles[r])
                }
                ))
            }
            snapshotCurrentStyles() {
                Object.keys(this._localTimelineStyles).forEach(e=>{
                    const t = this._localTimelineStyles[e];
                    this._pendingStyles[e] = t,
                    this._updateStyle(e, t)
                }
                )
            }
            getFinalKeyframe() {
                return this._keyframes.get(this.duration)
            }
            get properties() {
                const e = [];
                for (let t in this._currentKeyframe)
                    e.push(t);
                return e
            }
            mergeTimelineCollectedStyles(e) {
                Object.keys(e._styleSummary).forEach(t=>{
                    const r = this._styleSummary[t]
                      , i = e._styleSummary[t];
                    (!r || i.time > r.time) && this._updateStyle(t, i.value)
                }
                )
            }
            buildKeyframes() {
                this.applyStylesToKeyframe();
                const e = new Set
                  , t = new Set
                  , r = 1 === this._keyframes.size && 0 === this.duration;
                let i = [];
                this._keyframes.forEach((a,l)=>{
                    const u = Qn(a, !0);
                    Object.keys(u).forEach(c=>{
                        const d = u[c];
                        "!" == d ? e.add(c) : d == Nn && t.add(c)
                    }
                    ),
                    r || (u.offset = l / this.duration),
                    i.push(u)
                }
                );
                const o = e.size ? Ba(e.values()) : []
                  , s = t.size ? Ba(t.values()) : [];
                if (r) {
                    const a = i[0]
                      , l = Ci(a);
                    a.offset = 0,
                    l.offset = 1,
                    i = [a, l]
                }
                return of(this.element, i, o, s, this.duration, this.startTime, this.easing, !1)
            }
        }
        class KO extends Ka {
            constructor(e, t, r, i, o, s, a=!1) {
                super(e, t, s.delay),
                this.keyframes = r,
                this.preStyleProps = i,
                this.postStyleProps = o,
                this._stretchStartingKeyframe = a,
                this.timings = {
                    duration: s.duration,
                    delay: s.delay,
                    easing: s.easing
                }
            }
            containsAnimation() {
                return this.keyframes.length > 1
            }
            buildKeyframes() {
                let e = this.keyframes
                  , {delay: t, duration: r, easing: i} = this.timings;
                if (this._stretchStartingKeyframe && t) {
                    const o = []
                      , s = r + t
                      , a = t / s
                      , l = Qn(e[0], !1);
                    l.offset = 0,
                    o.push(l);
                    const u = Qn(e[0], !1);
                    u.offset = Jb(a),
                    o.push(u);
                    const c = e.length - 1;
                    for (let d = 1; d <= c; d++) {
                        let f = Qn(e[d], !1);
                        f.offset = Jb((t + f.offset * r) / s),
                        o.push(f)
                    }
                    r = s,
                    t = 0,
                    i = "",
                    e = o
                }
                return of(this.element, e, this.preStyleProps, this.postStyleProps, r, t, i, !0)
            }
        }
        function Jb(n, e=3) {
            const t = Math.pow(10, e - 1);
            return Math.round(n * t) / t
        }
        class lf {
        }
        class ZO extends lf {
            normalizePropertyName(e, t) {
                return tf(e)
            }
            normalizeStyleValue(e, t, r, i) {
                let o = "";
                const s = r.toString().trim();
                if (YO[t] && 0 !== r && "0" !== r)
                    if ("number" == typeof r)
                        o = "px";
                    else {
                        const a = r.match(/^[+-]?[\d\.]+([a-z]*)$/);
                        a && 0 == a[1].length && i.push(function G1(n, e) {
                            return new M(3005,K)
                        }())
                    }
                return s + o
            }
        }
        const YO = (()=>function XO(n) {
            const e = {};
            return n.forEach(t=>e[t] = !0),
            e
        }("width,height,minWidth,minHeight,maxWidth,maxHeight,left,top,bottom,right,fontSize,outlineWidth,outlineOffset,paddingTop,paddingLeft,paddingBottom,paddingRight,marginTop,marginLeft,marginBottom,marginRight,borderRadius,borderWidth,borderTopWidth,borderLeftWidth,borderRightWidth,borderBottomWidth,textIndent,perspective".split(",")))();
        function eD(n, e, t, r, i, o, s, a, l, u, c, d, f) {
            return {
                type: 0,
                element: n,
                triggerName: e,
                isRemovalTransition: i,
                fromState: t,
                fromStyles: o,
                toState: r,
                toStyles: s,
                timelines: a,
                queriedElements: l,
                preStyleProps: u,
                postStyleProps: c,
                totalTime: d,
                errors: f
            }
        }
        const uf = {};
        class tD {
            constructor(e, t, r) {
                this._triggerName = e,
                this.ast = t,
                this._stateStyles = r
            }
            match(e, t, r, i) {
                return function JO(n, e, t, r, i) {
                    return n.some(o=>o(e, t, r, i))
                }(this.ast.matchers, e, t, r, i)
            }
            buildStyles(e, t, r) {
                const i = this._stateStyles["*"]
                  , o = this._stateStyles[e]
                  , s = i ? i.buildStyles(t, r) : {};
                return o ? o.buildStyles(t, r) : s
            }
            build(e, t, r, i, o, s, a, l, u, c) {
                const d = []
                  , f = this.ast.options && this.ast.options.params || uf
                  , p = this.buildStyles(r, a && a.params || uf, d)
                  , m = l && l.params || uf
                  , y = this.buildStyles(i, m, d)
                  , _ = new Set
                  , g = new Map
                  , D = new Map
                  , I = "void" === i
                  , z = {
                    params: Object.assign(Object.assign({}, f), m)
                }
                  , ye = c ? [] : sf(e, t, this.ast.animation, o, s, p, y, z, u, d);
                let be = 0;
                if (ye.forEach(Mt=>{
                    be = Math.max(Mt.duration + Mt.delay, be)
                }
                ),
                d.length)
                    return eD(t, this._triggerName, r, i, I, p, y, [], [], g, D, be, d);
                ye.forEach(Mt=>{
                    const At = Mt.element
                      , Ti = Dt(g, At, {});
                    Mt.preStyleProps.forEach(nn=>Ti[nn] = !0);
                    const On = Dt(D, At, {});
                    Mt.postStyleProps.forEach(nn=>On[nn] = !0),
                    At !== t && _.add(At)
                }
                );
                const wt = Ba(_.values());
                return eD(t, this._triggerName, r, i, I, p, y, ye, wt, g, D, be)
            }
        }
        class ek {
            constructor(e, t, r) {
                this.styles = e,
                this.defaultParams = t,
                this.normalizer = r
            }
            buildStyles(e, t) {
                const r = {}
                  , i = Ci(this.defaultParams);
                return Object.keys(e).forEach(o=>{
                    const s = e[o];
                    null != s && (i[o] = s)
                }
                ),
                this.styles.styles.forEach(o=>{
                    if ("string" != typeof o) {
                        const s = o;
                        Object.keys(s).forEach(a=>{
                            let l = s[a];
                            l.length > 1 && (l = Va(l, i, t));
                            const u = this.normalizer.normalizePropertyName(a, t);
                            l = this.normalizer.normalizeStyleValue(a, u, l, t),
                            r[u] = l
                        }
                        )
                    }
                }
                ),
                r
            }
        }
        class nk {
            constructor(e, t, r) {
                this.name = e,
                this.ast = t,
                this._normalizer = r,
                this.transitionFactories = [],
                this.states = {},
                t.states.forEach(i=>{
                    this.states[i.name] = new ek(i.style,i.options && i.options.params || {},r)
                }
                ),
                nD(this.states, "true", "1"),
                nD(this.states, "false", "0"),
                t.transitions.forEach(i=>{
                    this.transitionFactories.push(new tD(e,i,this.states))
                }
                ),
                this.fallbackTransition = function rk(n, e, t) {
                    return new tD(n,{
                        type: 1,
                        animation: {
                            type: 2,
                            steps: [],
                            options: null
                        },
                        matchers: [(s,a)=>!0],
                        options: null,
                        queryCount: 0,
                        depCount: 0
                    },e)
                }(e, this.states)
            }
            get containsQueries() {
                return this.ast.queryCount > 0
            }
            matchTransition(e, t, r, i) {
                return this.transitionFactories.find(s=>s.match(e, t, r, i)) || null
            }
            matchStyles(e, t, r) {
                return this.fallbackTransition.buildStyles(e, t, r)
            }
        }
        function nD(n, e, t) {
            n.hasOwnProperty(e) ? n.hasOwnProperty(t) || (n[t] = n[e]) : n.hasOwnProperty(t) && (n[e] = n[t])
        }
        const ik = new qa;
        class ok {
            constructor(e, t, r) {
                this.bodyNode = e,
                this._driver = t,
                this._normalizer = r,
                this._animations = {},
                this._playersById = {},
                this.players = []
            }
            register(e, t) {
                const r = []
                  , o = nf(this._driver, t, r, []);
                if (r.length)
                    throw function lO(n) {
                        return new M(3503,K)
                    }();
                this._animations[e] = o
            }
            _buildPlayer(e, t, r) {
                const i = e.element
                  , o = kb(0, this._normalizer, 0, e.keyframes, t, r);
                return this._driver.animate(i, o, e.duration, e.delay, e.easing, [], !0)
            }
            create(e, t, r={}) {
                const i = []
                  , o = this._animations[e];
                let s;
                const a = new Map;
                if (o ? (s = sf(this._driver, t, o, Yd, ka, {}, {}, r, ik, i),
                s.forEach(c=>{
                    const d = Dt(a, c.element, {});
                    c.postStyleProps.forEach(f=>d[f] = null)
                }
                )) : (i.push(function uO() {
                    return new M(3300,K)
                }()),
                s = []),
                i.length)
                    throw function cO(n) {
                        return new M(3504,K)
                    }();
                a.forEach((c,d)=>{
                    Object.keys(c).forEach(f=>{
                        c[f] = this._driver.computeStyle(d, f, Nn)
                    }
                    )
                }
                );
                const u = Kn(s.map(c=>{
                    const d = a.get(c.element);
                    return this._buildPlayer(c, {}, d)
                }
                ));
                return this._playersById[e] = u,
                u.onDestroy(()=>this.destroy(e)),
                this.players.push(u),
                u
            }
            destroy(e) {
                const t = this._getPlayer(e);
                t.destroy(),
                delete this._playersById[e];
                const r = this.players.indexOf(t);
                r >= 0 && this.players.splice(r, 1)
            }
            _getPlayer(e) {
                const t = this._playersById[e];
                if (!t)
                    throw function dO(n) {
                        return new M(3301,K)
                    }();
                return t
            }
            listen(e, t, r, i) {
                const o = Wd(t, "", "", "");
                return zd(this._getPlayer(e), r, o, i),
                ()=>{}
            }
            command(e, t, r, i) {
                if ("register" == r)
                    return void this.register(e, i[0]);
                if ("create" == r)
                    return void this.create(e, t, i[0] || {});
                const o = this._getPlayer(e);
                switch (r) {
                case "play":
                    o.play();
                    break;
                case "pause":
                    o.pause();
                    break;
                case "reset":
                    o.reset();
                    break;
                case "restart":
                    o.restart();
                    break;
                case "finish":
                    o.finish();
                    break;
                case "init":
                    o.init();
                    break;
                case "setPosition":
                    o.setPosition(parseFloat(i[0]));
                    break;
                case "destroy":
                    this.destroy(e)
                }
            }
        }
        const rD = "ng-animate-queued"
          , cf = "ng-animate-disabled"
          , ck = []
          , iD = {
            namespaceId: "",
            setForRemoval: !1,
            setForMove: !1,
            hasAnimation: !1,
            removedBeforeQueried: !1
        }
          , dk = {
            namespaceId: "",
            setForMove: !1,
            setForRemoval: !1,
            hasAnimation: !1,
            removedBeforeQueried: !0
        }
          , jt = "__ng_removed";
        class df {
            constructor(e, t="") {
                this.namespaceId = t;
                const r = e && e.hasOwnProperty("value");
                if (this.value = function mk(n) {
                    return null != n ? n : null
                }(r ? e.value : e),
                r) {
                    const o = Ci(e);
                    delete o.value,
                    this.options = o
                } else
                    this.options = {};
                this.options.params || (this.options.params = {})
            }
            get params() {
                return this.options.params
            }
            absorbOptions(e) {
                const t = e.params;
                if (t) {
                    const r = this.options.params;
                    Object.keys(t).forEach(i=>{
                        null == r[i] && (r[i] = t[i])
                    }
                    )
                }
            }
        }
        const ko = "void"
          , ff = new df(ko);
        class fk {
            constructor(e, t, r) {
                this.id = e,
                this.hostElement = t,
                this._engine = r,
                this.players = [],
                this._triggers = {},
                this._queue = [],
                this._elementListeners = new Map,
                this._hostClassName = "ng-tns-" + e,
                Ht(t, this._hostClassName)
            }
            listen(e, t, r, i) {
                if (!this._triggers.hasOwnProperty(t))
                    throw function fO(n, e) {
                        return new M(3302,K)
                    }();
                if (null == r || 0 == r.length)
                    throw function hO(n) {
                        return new M(3303,K)
                    }();
                if (!function gk(n) {
                    return "start" == n || "done" == n
                }(r))
                    throw function pO(n, e) {
                        return new M(3400,K)
                    }();
                const o = Dt(this._elementListeners, e, [])
                  , s = {
                    name: t,
                    phase: r,
                    callback: i
                };
                o.push(s);
                const a = Dt(this._engine.statesByElement, e, {});
                return a.hasOwnProperty(t) || (Ht(e, Ra),
                Ht(e, Ra + "-" + t),
                a[t] = ff),
                ()=>{
                    this._engine.afterFlush(()=>{
                        const l = o.indexOf(s);
                        l >= 0 && o.splice(l, 1),
                        this._triggers[t] || delete a[t]
                    }
                    )
                }
            }
            register(e, t) {
                return !this._triggers[e] && (this._triggers[e] = t,
                !0)
            }
            _getTrigger(e) {
                const t = this._triggers[e];
                if (!t)
                    throw function mO(n) {
                        return new M(3401,K)
                    }();
                return t
            }
            trigger(e, t, r, i=!0) {
                const o = this._getTrigger(t)
                  , s = new hf(this.id,t,e);
                let a = this._engine.statesByElement.get(e);
                a || (Ht(e, Ra),
                Ht(e, Ra + "-" + t),
                this._engine.statesByElement.set(e, a = {}));
                let l = a[t];
                const u = new df(r,this.id);
                if (!(r && r.hasOwnProperty("value")) && l && u.absorbOptions(l.options),
                a[t] = u,
                l || (l = ff),
                u.value !== ko && l.value === u.value) {
                    if (!function vk(n, e) {
                        const t = Object.keys(n)
                          , r = Object.keys(e);
                        if (t.length != r.length)
                            return !1;
                        for (let i = 0; i < t.length; i++) {
                            const o = t[i];
                            if (!e.hasOwnProperty(o) || n[o] !== e[o])
                                return !1
                        }
                        return !0
                    }(l.params, u.params)) {
                        const m = []
                          , y = o.matchStyles(l.value, l.params, m)
                          , _ = o.matchStyles(u.value, u.params, m);
                        m.length ? this._engine.reportError(m) : this._engine.afterFlush(()=>{
                            Mr(e, y),
                            vn(e, _)
                        }
                        )
                    }
                    return
                }
                const f = Dt(this._engine.playersByElement, e, []);
                f.forEach(m=>{
                    m.namespaceId == this.id && m.triggerName == t && m.queued && m.destroy()
                }
                );
                let h = o.matchTransition(l.value, u.value, e, u.params)
                  , p = !1;
                if (!h) {
                    if (!i)
                        return;
                    h = o.fallbackTransition,
                    p = !0
                }
                return this._engine.totalQueuedPlayers++,
                this._queue.push({
                    element: e,
                    triggerName: t,
                    transition: h,
                    fromState: l,
                    toState: u,
                    player: s,
                    isFallbackTransition: p
                }),
                p || (Ht(e, rD),
                s.onStart(()=>{
                    Ei(e, rD)
                }
                )),
                s.onDone(()=>{
                    let m = this.players.indexOf(s);
                    m >= 0 && this.players.splice(m, 1);
                    const y = this._engine.playersByElement.get(e);
                    if (y) {
                        let _ = y.indexOf(s);
                        _ >= 0 && y.splice(_, 1)
                    }
                }
                ),
                this.players.push(s),
                f.push(s),
                s
            }
            deregister(e) {
                delete this._triggers[e],
                this._engine.statesByElement.forEach((t,r)=>{
                    delete t[e]
                }
                ),
                this._elementListeners.forEach((t,r)=>{
                    this._elementListeners.set(r, t.filter(i=>i.name != e))
                }
                )
            }
            clearElementCache(e) {
                this._engine.statesByElement.delete(e),
                this._elementListeners.delete(e);
                const t = this._engine.playersByElement.get(e);
                t && (t.forEach(r=>r.destroy()),
                this._engine.playersByElement.delete(e))
            }
            _signalRemovalForInnerTriggers(e, t) {
                const r = this._engine.driver.query(e, Pa, !0);
                r.forEach(i=>{
                    if (i[jt])
                        return;
                    const o = this._engine.fetchNamespacesByElement(i);
                    o.size ? o.forEach(s=>s.triggerLeaveAnimation(i, t, !1, !0)) : this.clearElementCache(i)
                }
                ),
                this._engine.afterFlushAnimationsDone(()=>r.forEach(i=>this.clearElementCache(i)))
            }
            triggerLeaveAnimation(e, t, r, i) {
                const o = this._engine.statesByElement.get(e)
                  , s = new Map;
                if (o) {
                    const a = [];
                    if (Object.keys(o).forEach(l=>{
                        if (s.set(l, o[l].value),
                        this._triggers[l]) {
                            const u = this.trigger(e, l, ko, i);
                            u && a.push(u)
                        }
                    }
                    ),
                    a.length)
                        return this._engine.markElementAsRemoved(this.id, e, !0, t, s),
                        r && Kn(a).onDone(()=>this._engine.processLeaveNode(e)),
                        !0
                }
                return !1
            }
            prepareLeaveAnimationListeners(e) {
                const t = this._elementListeners.get(e)
                  , r = this._engine.statesByElement.get(e);
                if (t && r) {
                    const i = new Set;
                    t.forEach(o=>{
                        const s = o.name;
                        if (i.has(s))
                            return;
                        i.add(s);
                        const l = this._triggers[s].fallbackTransition
                          , u = r[s] || ff
                          , c = new df(ko)
                          , d = new hf(this.id,s,e);
                        this._engine.totalQueuedPlayers++,
                        this._queue.push({
                            element: e,
                            triggerName: s,
                            transition: l,
                            fromState: u,
                            toState: c,
                            player: d,
                            isFallbackTransition: !0
                        })
                    }
                    )
                }
            }
            removeNode(e, t) {
                const r = this._engine;
                if (e.childElementCount && this._signalRemovalForInnerTriggers(e, t),
                this.triggerLeaveAnimation(e, t, !0))
                    return;
                let i = !1;
                if (r.totalAnimations) {
                    const o = r.players.length ? r.playersByQueriedElement.get(e) : [];
                    if (o && o.length)
                        i = !0;
                    else {
                        let s = e;
                        for (; s = s.parentNode; )
                            if (r.statesByElement.get(s)) {
                                i = !0;
                                break
                            }
                    }
                }
                if (this.prepareLeaveAnimationListeners(e),
                i)
                    r.markElementAsRemoved(this.id, e, !1, t);
                else {
                    const o = e[jt];
                    (!o || o === iD) && (r.afterFlush(()=>this.clearElementCache(e)),
                    r.destroyInnerAnimations(e),
                    r._onRemovalComplete(e, t))
                }
            }
            insertNode(e, t) {
                Ht(e, this._hostClassName)
            }
            drainQueuedTransitions(e) {
                const t = [];
                return this._queue.forEach(r=>{
                    const i = r.player;
                    if (i.destroyed)
                        return;
                    const o = r.element
                      , s = this._elementListeners.get(o);
                    s && s.forEach(a=>{
                        if (a.name == r.triggerName) {
                            const l = Wd(o, r.triggerName, r.fromState.value, r.toState.value);
                            l._data = e,
                            zd(r.player, a.phase, l, a.callback)
                        }
                    }
                    ),
                    i.markedForDestroy ? this._engine.afterFlush(()=>{
                        i.destroy()
                    }
                    ) : t.push(r)
                }
                ),
                this._queue = [],
                t.sort((r,i)=>{
                    const o = r.transition.ast.depCount
                      , s = i.transition.ast.depCount;
                    return 0 == o || 0 == s ? o - s : this._engine.driver.containsElement(r.element, i.element) ? 1 : -1
                }
                )
            }
            destroy(e) {
                this.players.forEach(t=>t.destroy()),
                this._signalRemovalForInnerTriggers(this.hostElement, e)
            }
            elementContainsData(e) {
                let t = !1;
                return this._elementListeners.has(e) && (t = !0),
                t = !!this._queue.find(r=>r.element === e) || t,
                t
            }
        }
        class hk {
            constructor(e, t, r) {
                this.bodyNode = e,
                this.driver = t,
                this._normalizer = r,
                this.players = [],
                this.newHostElements = new Map,
                this.playersByElement = new Map,
                this.playersByQueriedElement = new Map,
                this.statesByElement = new Map,
                this.disabledNodes = new Set,
                this.totalAnimations = 0,
                this.totalQueuedPlayers = 0,
                this._namespaceLookup = {},
                this._namespaceList = [],
                this._flushFns = [],
                this._whenQuietFns = [],
                this.namespacesByHostElement = new Map,
                this.collectedEnterElements = [],
                this.collectedLeaveElements = [],
                this.onRemovalComplete = (i,o)=>{}
            }
            _onRemovalComplete(e, t) {
                this.onRemovalComplete(e, t)
            }
            get queuedPlayers() {
                const e = [];
                return this._namespaceList.forEach(t=>{
                    t.players.forEach(r=>{
                        r.queued && e.push(r)
                    }
                    )
                }
                ),
                e
            }
            createNamespace(e, t) {
                const r = new fk(e,t,this);
                return this.bodyNode && this.driver.containsElement(this.bodyNode, t) ? this._balanceNamespaceList(r, t) : (this.newHostElements.set(t, r),
                this.collectEnterElement(t)),
                this._namespaceLookup[e] = r
            }
            _balanceNamespaceList(e, t) {
                const r = this._namespaceList
                  , i = this.namespacesByHostElement
                  , o = r.length - 1;
                if (o >= 0) {
                    let s = !1;
                    if (void 0 !== this.driver.getParentElement) {
                        let a = this.driver.getParentElement(t);
                        for (; a; ) {
                            const l = i.get(a);
                            if (l) {
                                const u = r.indexOf(l);
                                r.splice(u + 1, 0, e),
                                s = !0;
                                break
                            }
                            a = this.driver.getParentElement(a)
                        }
                    } else
                        for (let a = o; a >= 0; a--)
                            if (this.driver.containsElement(r[a].hostElement, t)) {
                                r.splice(a + 1, 0, e),
                                s = !0;
                                break
                            }
                    s || r.unshift(e)
                } else
                    r.push(e);
                return i.set(t, e),
                e
            }
            register(e, t) {
                let r = this._namespaceLookup[e];
                return r || (r = this.createNamespace(e, t)),
                r
            }
            registerTrigger(e, t, r) {
                let i = this._namespaceLookup[e];
                i && i.register(t, r) && this.totalAnimations++
            }
            destroy(e, t) {
                if (!e)
                    return;
                const r = this._fetchNamespace(e);
                this.afterFlush(()=>{
                    this.namespacesByHostElement.delete(r.hostElement),
                    delete this._namespaceLookup[e];
                    const i = this._namespaceList.indexOf(r);
                    i >= 0 && this._namespaceList.splice(i, 1)
                }
                ),
                this.afterFlushAnimationsDone(()=>r.destroy(t))
            }
            _fetchNamespace(e) {
                return this._namespaceLookup[e]
            }
            fetchNamespacesByElement(e) {
                const t = new Set
                  , r = this.statesByElement.get(e);
                if (r) {
                    const i = Object.keys(r);
                    for (let o = 0; o < i.length; o++) {
                        const s = r[i[o]].namespaceId;
                        if (s) {
                            const a = this._fetchNamespace(s);
                            a && t.add(a)
                        }
                    }
                }
                return t
            }
            trigger(e, t, r, i) {
                if (Qa(t)) {
                    const o = this._fetchNamespace(e);
                    if (o)
                        return o.trigger(t, r, i),
                        !0
                }
                return !1
            }
            insertNode(e, t, r, i) {
                if (!Qa(t))
                    return;
                const o = t[jt];
                if (o && o.setForRemoval) {
                    o.setForRemoval = !1,
                    o.setForMove = !0;
                    const s = this.collectedLeaveElements.indexOf(t);
                    s >= 0 && this.collectedLeaveElements.splice(s, 1)
                }
                if (e) {
                    const s = this._fetchNamespace(e);
                    s && s.insertNode(t, r)
                }
                i && this.collectEnterElement(t)
            }
            collectEnterElement(e) {
                this.collectedEnterElements.push(e)
            }
            markElementAsDisabled(e, t) {
                t ? this.disabledNodes.has(e) || (this.disabledNodes.add(e),
                Ht(e, cf)) : this.disabledNodes.has(e) && (this.disabledNodes.delete(e),
                Ei(e, cf))
            }
            removeNode(e, t, r, i) {
                if (Qa(t)) {
                    const o = e ? this._fetchNamespace(e) : null;
                    if (o ? o.removeNode(t, i) : this.markElementAsRemoved(e, t, !1, i),
                    r) {
                        const s = this.namespacesByHostElement.get(t);
                        s && s.id !== e && s.removeNode(t, i)
                    }
                } else
                    this._onRemovalComplete(t, i)
            }
            markElementAsRemoved(e, t, r, i, o) {
                this.collectedLeaveElements.push(t),
                t[jt] = {
                    namespaceId: e,
                    setForRemoval: i,
                    hasAnimation: r,
                    removedBeforeQueried: !1,
                    previousTriggersValues: o
                }
            }
            listen(e, t, r, i, o) {
                return Qa(t) ? this._fetchNamespace(e).listen(t, r, i, o) : ()=>{}
            }
            _buildInstruction(e, t, r, i, o) {
                return e.transition.build(this.driver, e.element, e.fromState.value, e.toState.value, r, i, e.fromState.options, e.toState.options, t, o)
            }
            destroyInnerAnimations(e) {
                let t = this.driver.query(e, Pa, !0);
                t.forEach(r=>this.destroyActiveAnimationsForElement(r)),
                0 != this.playersByQueriedElement.size && (t = this.driver.query(e, Xd, !0),
                t.forEach(r=>this.finishActiveQueriedAnimationOnElement(r)))
            }
            destroyActiveAnimationsForElement(e) {
                const t = this.playersByElement.get(e);
                t && t.forEach(r=>{
                    r.queued ? r.markedForDestroy = !0 : r.destroy()
                }
                )
            }
            finishActiveQueriedAnimationOnElement(e) {
                const t = this.playersByQueriedElement.get(e);
                t && t.forEach(r=>r.finish())
            }
            whenRenderingDone() {
                return new Promise(e=>{
                    if (this.players.length)
                        return Kn(this.players).onDone(()=>e());
                    e()
                }
                )
            }
            processLeaveNode(e) {
                var t;
                const r = e[jt];
                if (r && r.setForRemoval) {
                    if (e[jt] = iD,
                    r.namespaceId) {
                        this.destroyInnerAnimations(e);
                        const i = this._fetchNamespace(r.namespaceId);
                        i && i.clearElementCache(e)
                    }
                    this._onRemovalComplete(e, r.setForRemoval)
                }
                (null === (t = e.classList) || void 0 === t ? void 0 : t.contains(cf)) && this.markElementAsDisabled(e, !1),
                this.driver.query(e, ".ng-animate-disabled", !0).forEach(i=>{
                    this.markElementAsDisabled(i, !1)
                }
                )
            }
            flush(e=-1) {
                let t = [];
                if (this.newHostElements.size && (this.newHostElements.forEach((r,i)=>this._balanceNamespaceList(r, i)),
                this.newHostElements.clear()),
                this.totalAnimations && this.collectedEnterElements.length)
                    for (let r = 0; r < this.collectedEnterElements.length; r++)
                        Ht(this.collectedEnterElements[r], "ng-star-inserted");
                if (this._namespaceList.length && (this.totalQueuedPlayers || this.collectedLeaveElements.length)) {
                    const r = [];
                    try {
                        t = this._flushAnimations(r, e)
                    } finally {
                        for (let i = 0; i < r.length; i++)
                            r[i]()
                    }
                } else
                    for (let r = 0; r < this.collectedLeaveElements.length; r++)
                        this.processLeaveNode(this.collectedLeaveElements[r]);
                if (this.totalQueuedPlayers = 0,
                this.collectedEnterElements.length = 0,
                this.collectedLeaveElements.length = 0,
                this._flushFns.forEach(r=>r()),
                this._flushFns = [],
                this._whenQuietFns.length) {
                    const r = this._whenQuietFns;
                    this._whenQuietFns = [],
                    t.length ? Kn(t).onDone(()=>{
                        r.forEach(i=>i())
                    }
                    ) : r.forEach(i=>i())
                }
            }
            reportError(e) {
                throw function gO(n) {
                    return new M(3402,K)
                }()
            }
            _flushAnimations(e, t) {
                const r = new qa
                  , i = []
                  , o = new Map
                  , s = []
                  , a = new Map
                  , l = new Map
                  , u = new Map
                  , c = new Set;
                this.disabledNodes.forEach(T=>{
                    c.add(T);
                    const F = this.driver.query(T, ".ng-animate-queued", !0);
                    for (let k = 0; k < F.length; k++)
                        c.add(F[k])
                }
                );
                const d = this.bodyNode
                  , f = Array.from(this.statesByElement.keys())
                  , h = aD(f, this.collectedEnterElements)
                  , p = new Map;
                let m = 0;
                h.forEach((T,F)=>{
                    const k = Yd + m++;
                    p.set(F, k),
                    T.forEach(J=>Ht(J, k))
                }
                );
                const y = []
                  , _ = new Set
                  , g = new Set;
                for (let T = 0; T < this.collectedLeaveElements.length; T++) {
                    const F = this.collectedLeaveElements[T]
                      , k = F[jt];
                    k && k.setForRemoval && (y.push(F),
                    _.add(F),
                    k.hasAnimation ? this.driver.query(F, ".ng-star-inserted", !0).forEach(J=>_.add(J)) : g.add(F))
                }
                const D = new Map
                  , I = aD(f, Array.from(_));
                I.forEach((T,F)=>{
                    const k = ka + m++;
                    D.set(F, k),
                    T.forEach(J=>Ht(J, k))
                }
                ),
                e.push(()=>{
                    h.forEach((T,F)=>{
                        const k = p.get(F);
                        T.forEach(J=>Ei(J, k))
                    }
                    ),
                    I.forEach((T,F)=>{
                        const k = D.get(F);
                        T.forEach(J=>Ei(J, k))
                    }
                    ),
                    y.forEach(T=>{
                        this.processLeaveNode(T)
                    }
                    )
                }
                );
                const z = []
                  , ye = [];
                for (let T = this._namespaceList.length - 1; T >= 0; T--)
                    this._namespaceList[T].drainQueuedTransitions(t).forEach(k=>{
                        const J = k.player
                          , He = k.element;
                        if (z.push(J),
                        this.collectedEnterElements.length) {
                            const ot = He[jt];
                            if (ot && ot.setForMove) {
                                if (ot.previousTriggersValues && ot.previousTriggersValues.has(k.triggerName)) {
                                    const Sr = ot.previousTriggersValues.get(k.triggerName)
                                      , er = this.statesByElement.get(k.element);
                                    er && er[k.triggerName] && (er[k.triggerName].value = Sr)
                                }
                                return void J.destroy()
                            }
                        }
                        const bn = !d || !this.driver.containsElement(d, He)
                          , Tt = D.get(He)
                          , Jn = p.get(He)
                          , De = this._buildInstruction(k, r, Jn, Tt, bn);
                        if (De.errors && De.errors.length)
                            return void ye.push(De);
                        if (bn)
                            return J.onStart(()=>Mr(He, De.fromStyles)),
                            J.onDestroy(()=>vn(He, De.toStyles)),
                            void i.push(J);
                        if (k.isFallbackTransition)
                            return J.onStart(()=>Mr(He, De.fromStyles)),
                            J.onDestroy(()=>vn(He, De.toStyles)),
                            void i.push(J);
                        const JD = [];
                        De.timelines.forEach(ot=>{
                            ot.stretchStartingKeyframe = !0,
                            this.disabledNodes.has(ot.element) || JD.push(ot)
                        }
                        ),
                        De.timelines = JD,
                        r.append(He, De.timelines),
                        s.push({
                            instruction: De,
                            player: J,
                            element: He
                        }),
                        De.queriedElements.forEach(ot=>Dt(a, ot, []).push(J)),
                        De.preStyleProps.forEach((ot,Sr)=>{
                            const er = Object.keys(ot);
                            if (er.length) {
                                let xr = l.get(Sr);
                                xr || l.set(Sr, xr = new Set),
                                er.forEach(Mf=>xr.add(Mf))
                            }
                        }
                        ),
                        De.postStyleProps.forEach((ot,Sr)=>{
                            const er = Object.keys(ot);
                            let xr = u.get(Sr);
                            xr || u.set(Sr, xr = new Set),
                            er.forEach(Mf=>xr.add(Mf))
                        }
                        )
                    }
                    );
                if (ye.length) {
                    const T = [];
                    ye.forEach(F=>{
                        T.push(function yO(n, e) {
                            return new M(3505,K)
                        }())
                    }
                    ),
                    z.forEach(F=>F.destroy()),
                    this.reportError(T)
                }
                const be = new Map
                  , wt = new Map;
                s.forEach(T=>{
                    const F = T.element;
                    r.has(F) && (wt.set(F, F),
                    this._beforeAnimationBuild(T.player.namespaceId, T.instruction, be))
                }
                ),
                i.forEach(T=>{
                    const F = T.element;
                    this._getPreviousPlayers(F, !1, T.namespaceId, T.triggerName, null).forEach(J=>{
                        Dt(be, F, []).push(J),
                        J.destroy()
                    }
                    )
                }
                );
                const Mt = y.filter(T=>uD(T, l, u))
                  , At = new Map;
                sD(At, this.driver, g, u, Nn).forEach(T=>{
                    uD(T, l, u) && Mt.push(T)
                }
                );
                const On = new Map;
                h.forEach((T,F)=>{
                    sD(On, this.driver, new Set(T), l, "!")
                }
                ),
                Mt.forEach(T=>{
                    const F = At.get(T)
                      , k = On.get(T);
                    At.set(T, Object.assign(Object.assign({}, F), k))
                }
                );
                const nn = []
                  , Ii = []
                  , Si = {};
                s.forEach(T=>{
                    const {element: F, player: k, instruction: J} = T;
                    if (r.has(F)) {
                        if (c.has(F))
                            return k.onDestroy(()=>vn(F, J.toStyles)),
                            k.disabled = !0,
                            k.overrideTotalTime(J.totalTime),
                            void i.push(k);
                        let He = Si;
                        if (wt.size > 1) {
                            let Tt = F;
                            const Jn = [];
                            for (; Tt = Tt.parentNode; ) {
                                const De = wt.get(Tt);
                                if (De) {
                                    He = De;
                                    break
                                }
                                Jn.push(Tt)
                            }
                            Jn.forEach(De=>wt.set(De, He))
                        }
                        const bn = this._buildAnimation(k.namespaceId, J, be, o, On, At);
                        if (k.setRealPlayer(bn),
                        He === Si)
                            nn.push(k);
                        else {
                            const Tt = this.playersByElement.get(He);
                            Tt && Tt.length && (k.parentPlayer = Kn(Tt)),
                            i.push(k)
                        }
                    } else
                        Mr(F, J.fromStyles),
                        k.onDestroy(()=>vn(F, J.toStyles)),
                        Ii.push(k),
                        c.has(F) && i.push(k)
                }
                ),
                Ii.forEach(T=>{
                    const F = o.get(T.element);
                    if (F && F.length) {
                        const k = Kn(F);
                        T.setRealPlayer(k)
                    }
                }
                ),
                i.forEach(T=>{
                    T.parentPlayer ? T.syncPlayerEvents(T.parentPlayer) : T.destroy()
                }
                );
                for (let T = 0; T < y.length; T++) {
                    const F = y[T]
                      , k = F[jt];
                    if (Ei(F, ka),
                    k && k.hasAnimation)
                        continue;
                    let J = [];
                    if (a.size) {
                        let bn = a.get(F);
                        bn && bn.length && J.push(...bn);
                        let Tt = this.driver.query(F, Xd, !0);
                        for (let Jn = 0; Jn < Tt.length; Jn++) {
                            let De = a.get(Tt[Jn]);
                            De && De.length && J.push(...De)
                        }
                    }
                    const He = J.filter(bn=>!bn.destroyed);
                    He.length ? yk(this, F, He) : this.processLeaveNode(F)
                }
                return y.length = 0,
                nn.forEach(T=>{
                    this.players.push(T),
                    T.onDone(()=>{
                        T.destroy();
                        const F = this.players.indexOf(T);
                        this.players.splice(F, 1)
                    }
                    ),
                    T.play()
                }
                ),
                nn
            }
            elementContainsData(e, t) {
                let r = !1;
                const i = t[jt];
                return i && i.setForRemoval && (r = !0),
                this.playersByElement.has(t) && (r = !0),
                this.playersByQueriedElement.has(t) && (r = !0),
                this.statesByElement.has(t) && (r = !0),
                this._fetchNamespace(e).elementContainsData(t) || r
            }
            afterFlush(e) {
                this._flushFns.push(e)
            }
            afterFlushAnimationsDone(e) {
                this._whenQuietFns.push(e)
            }
            _getPreviousPlayers(e, t, r, i, o) {
                let s = [];
                if (t) {
                    const a = this.playersByQueriedElement.get(e);
                    a && (s = a)
                } else {
                    const a = this.playersByElement.get(e);
                    if (a) {
                        const l = !o || o == ko;
                        a.forEach(u=>{
                            u.queued || !l && u.triggerName != i || s.push(u)
                        }
                        )
                    }
                }
                return (r || i) && (s = s.filter(a=>!(r && r != a.namespaceId || i && i != a.triggerName))),
                s
            }
            _beforeAnimationBuild(e, t, r) {
                const o = t.element
                  , s = t.isRemovalTransition ? void 0 : e
                  , a = t.isRemovalTransition ? void 0 : t.triggerName;
                for (const l of t.timelines) {
                    const u = l.element
                      , c = u !== o
                      , d = Dt(r, u, []);
                    this._getPreviousPlayers(u, c, s, a, t.toState).forEach(h=>{
                        const p = h.getRealPlayer();
                        p.beforeDestroy && p.beforeDestroy(),
                        h.destroy(),
                        d.push(h)
                    }
                    )
                }
                Mr(o, t.fromStyles)
            }
            _buildAnimation(e, t, r, i, o, s) {
                const a = t.triggerName
                  , l = t.element
                  , u = []
                  , c = new Set
                  , d = new Set
                  , f = t.timelines.map(p=>{
                    const m = p.element;
                    c.add(m);
                    const y = m[jt];
                    if (y && y.removedBeforeQueried)
                        return new No(p.duration,p.delay);
                    const _ = m !== l
                      , g = function _k(n) {
                        const e = [];
                        return lD(n, e),
                        e
                    }((r.get(m) || ck).map(be=>be.getRealPlayer())).filter(be=>!!be.element && be.element === m)
                      , D = o.get(m)
                      , I = s.get(m)
                      , z = kb(0, this._normalizer, 0, p.keyframes, D, I)
                      , ye = this._buildPlayer(p, z, g);
                    if (p.subTimeline && i && d.add(m),
                    _) {
                        const be = new hf(e,a,m);
                        be.setRealPlayer(ye),
                        u.push(be)
                    }
                    return ye
                }
                );
                u.forEach(p=>{
                    Dt(this.playersByQueriedElement, p.element, []).push(p),
                    p.onDone(()=>function pk(n, e, t) {
                        let r;
                        if (n instanceof Map) {
                            if (r = n.get(e),
                            r) {
                                if (r.length) {
                                    const i = r.indexOf(t);
                                    r.splice(i, 1)
                                }
                                0 == r.length && n.delete(e)
                            }
                        } else if (r = n[e],
                        r) {
                            if (r.length) {
                                const i = r.indexOf(t);
                                r.splice(i, 1)
                            }
                            0 == r.length && delete n[e]
                        }
                        return r
                    }(this.playersByQueriedElement, p.element, p))
                }
                ),
                c.forEach(p=>Ht(p, Gb));
                const h = Kn(f);
                return h.onDestroy(()=>{
                    c.forEach(p=>Ei(p, Gb)),
                    vn(l, t.toStyles)
                }
                ),
                d.forEach(p=>{
                    Dt(i, p, []).push(h)
                }
                ),
                h
            }
            _buildPlayer(e, t, r) {
                return t.length > 0 ? this.driver.animate(e.element, t, e.duration, e.delay, e.easing, r) : new No(e.duration,e.delay)
            }
        }
        class hf {
            constructor(e, t, r) {
                this.namespaceId = e,
                this.triggerName = t,
                this.element = r,
                this._player = new No,
                this._containsRealPlayer = !1,
                this._queuedCallbacks = {},
                this.destroyed = !1,
                this.markedForDestroy = !1,
                this.disabled = !1,
                this.queued = !0,
                this.totalTime = 0
            }
            setRealPlayer(e) {
                this._containsRealPlayer || (this._player = e,
                Object.keys(this._queuedCallbacks).forEach(t=>{
                    this._queuedCallbacks[t].forEach(r=>zd(e, t, void 0, r))
                }
                ),
                this._queuedCallbacks = {},
                this._containsRealPlayer = !0,
                this.overrideTotalTime(e.totalTime),
                this.queued = !1)
            }
            getRealPlayer() {
                return this._player
            }
            overrideTotalTime(e) {
                this.totalTime = e
            }
            syncPlayerEvents(e) {
                const t = this._player;
                t.triggerCallback && e.onStart(()=>t.triggerCallback("start")),
                e.onDone(()=>this.finish()),
                e.onDestroy(()=>this.destroy())
            }
            _queueEvent(e, t) {
                Dt(this._queuedCallbacks, e, []).push(t)
            }
            onDone(e) {
                this.queued && this._queueEvent("done", e),
                this._player.onDone(e)
            }
            onStart(e) {
                this.queued && this._queueEvent("start", e),
                this._player.onStart(e)
            }
            onDestroy(e) {
                this.queued && this._queueEvent("destroy", e),
                this._player.onDestroy(e)
            }
            init() {
                this._player.init()
            }
            hasStarted() {
                return !this.queued && this._player.hasStarted()
            }
            play() {
                !this.queued && this._player.play()
            }
            pause() {
                !this.queued && this._player.pause()
            }
            restart() {
                !this.queued && this._player.restart()
            }
            finish() {
                this._player.finish()
            }
            destroy() {
                this.destroyed = !0,
                this._player.destroy()
            }
            reset() {
                !this.queued && this._player.reset()
            }
            setPosition(e) {
                this.queued || this._player.setPosition(e)
            }
            getPosition() {
                return this.queued ? 0 : this._player.getPosition()
            }
            triggerCallback(e) {
                const t = this._player;
                t.triggerCallback && t.triggerCallback(e)
            }
        }
        function Qa(n) {
            return n && 1 === n.nodeType
        }
        function oD(n, e) {
            const t = n.style.display;
            return n.style.display = null != e ? e : "none",
            t
        }
        function sD(n, e, t, r, i) {
            const o = [];
            t.forEach(l=>o.push(oD(l)));
            const s = [];
            r.forEach((l,u)=>{
                const c = {};
                l.forEach(d=>{
                    const f = c[d] = e.computeStyle(u, d, i);
                    (!f || 0 == f.length) && (u[jt] = dk,
                    s.push(u))
                }
                ),
                n.set(u, c)
            }
            );
            let a = 0;
            return t.forEach(l=>oD(l, o[a++])),
            s
        }
        function aD(n, e) {
            const t = new Map;
            if (n.forEach(a=>t.set(a, [])),
            0 == e.length)
                return t;
            const i = new Set(e)
              , o = new Map;
            function s(a) {
                if (!a)
                    return 1;
                let l = o.get(a);
                if (l)
                    return l;
                const u = a.parentNode;
                return l = t.has(u) ? u : i.has(u) ? 1 : s(u),
                o.set(a, l),
                l
            }
            return e.forEach(a=>{
                const l = s(a);
                1 !== l && t.get(l).push(a)
            }
            ),
            t
        }
        function Ht(n, e) {
            var t;
            null === (t = n.classList) || void 0 === t || t.add(e)
        }
        function Ei(n, e) {
            var t;
            null === (t = n.classList) || void 0 === t || t.remove(e)
        }
        function yk(n, e, t) {
            Kn(t).onDone(()=>n.processLeaveNode(e))
        }
        function lD(n, e) {
            for (let t = 0; t < n.length; t++) {
                const r = n[t];
                r instanceof Nb ? lD(r.players, e) : e.push(r)
            }
        }
        function uD(n, e, t) {
            const r = t.get(n);
            if (!r)
                return !1;
            let i = e.get(n);
            return i ? r.forEach(o=>i.add(o)) : e.set(n, r),
            t.delete(n),
            !0
        }
        class Za {
            constructor(e, t, r) {
                this.bodyNode = e,
                this._driver = t,
                this._normalizer = r,
                this._triggerCache = {},
                this.onRemovalComplete = (i,o)=>{}
                ,
                this._transitionEngine = new hk(e,t,r),
                this._timelineEngine = new ok(e,t,r),
                this._transitionEngine.onRemovalComplete = (i,o)=>this.onRemovalComplete(i, o)
            }
            registerTrigger(e, t, r, i, o) {
                const s = e + "-" + i;
                let a = this._triggerCache[s];
                if (!a) {
                    const l = []
                      , c = nf(this._driver, o, l, []);
                    if (l.length)
                        throw function sO(n, e) {
                            return new M(3404,K)
                        }();
                    a = function tk(n, e, t) {
                        return new nk(n,e,t)
                    }(i, c, this._normalizer),
                    this._triggerCache[s] = a
                }
                this._transitionEngine.registerTrigger(t, i, a)
            }
            register(e, t) {
                this._transitionEngine.register(e, t)
            }
            destroy(e, t) {
                this._transitionEngine.destroy(e, t)
            }
            onInsert(e, t, r, i) {
                this._transitionEngine.insertNode(e, t, r, i)
            }
            onRemove(e, t, r, i) {
                this._transitionEngine.removeNode(e, t, i || !1, r)
            }
            disableAnimations(e, t) {
                this._transitionEngine.markElementAsDisabled(e, t)
            }
            process(e, t, r, i) {
                if ("@" == r.charAt(0)) {
                    const [o,s] = Rb(r);
                    this._timelineEngine.command(o, t, s, i)
                } else
                    this._transitionEngine.trigger(e, t, r, i)
            }
            listen(e, t, r, i, o) {
                if ("@" == r.charAt(0)) {
                    const [s,a] = Rb(r);
                    return this._timelineEngine.listen(s, t, a, o)
                }
                return this._transitionEngine.listen(e, t, r, i, o)
            }
            flush(e=-1) {
                this._transitionEngine.flush(e)
            }
            get players() {
                return this._transitionEngine.players.concat(this._timelineEngine.players)
            }
            whenRenderingDone() {
                return this._transitionEngine.whenRenderingDone()
            }
        }
        let Dk = (()=>{
            class n {
                constructor(t, r, i) {
                    this._element = t,
                    this._startStyles = r,
                    this._endStyles = i,
                    this._state = 0;
                    let o = n.initialStylesByElement.get(t);
                    o || n.initialStylesByElement.set(t, o = {}),
                    this._initialStyles = o
                }
                start() {
                    this._state < 1 && (this._startStyles && vn(this._element, this._startStyles, this._initialStyles),
                    this._state = 1)
                }
                finish() {
                    this.start(),
                    this._state < 2 && (vn(this._element, this._initialStyles),
                    this._endStyles && (vn(this._element, this._endStyles),
                    this._endStyles = null),
                    this._state = 1)
                }
                destroy() {
                    this.finish(),
                    this._state < 3 && (n.initialStylesByElement.delete(this._element),
                    this._startStyles && (Mr(this._element, this._startStyles),
                    this._endStyles = null),
                    this._endStyles && (Mr(this._element, this._endStyles),
                    this._endStyles = null),
                    vn(this._element, this._initialStyles),
                    this._state = 3)
                }
            }
            return n.initialStylesByElement = new WeakMap,
            n
        }
        )();
        function pf(n) {
            let e = null;
            const t = Object.keys(n);
            for (let r = 0; r < t.length; r++) {
                const i = t[r];
                Ck(i) && (e = e || {},
                e[i] = n[i])
            }
            return e
        }
        function Ck(n) {
            return "display" === n || "position" === n
        }
        class cD {
            constructor(e, t, r, i) {
                this.element = e,
                this.keyframes = t,
                this.options = r,
                this._specialStyles = i,
                this._onDoneFns = [],
                this._onStartFns = [],
                this._onDestroyFns = [],
                this._initialized = !1,
                this._finished = !1,
                this._started = !1,
                this._destroyed = !1,
                this.time = 0,
                this.parentPlayer = null,
                this.currentSnapshot = {},
                this._duration = r.duration,
                this._delay = r.delay || 0,
                this.time = this._duration + this._delay
            }
            _onFinish() {
                this._finished || (this._finished = !0,
                this._onDoneFns.forEach(e=>e()),
                this._onDoneFns = [])
            }
            init() {
                this._buildPlayer(),
                this._preparePlayerBeforeStart()
            }
            _buildPlayer() {
                if (this._initialized)
                    return;
                this._initialized = !0;
                const e = this.keyframes;
                this.domPlayer = this._triggerWebAnimation(this.element, e, this.options),
                this._finalKeyframe = e.length ? e[e.length - 1] : {},
                this.domPlayer.addEventListener("finish", ()=>this._onFinish())
            }
            _preparePlayerBeforeStart() {
                this._delay ? this._resetDomPlayerState() : this.domPlayer.pause()
            }
            _triggerWebAnimation(e, t, r) {
                return e.animate(t, r)
            }
            onStart(e) {
                this._onStartFns.push(e)
            }
            onDone(e) {
                this._onDoneFns.push(e)
            }
            onDestroy(e) {
                this._onDestroyFns.push(e)
            }
            play() {
                this._buildPlayer(),
                this.hasStarted() || (this._onStartFns.forEach(e=>e()),
                this._onStartFns = [],
                this._started = !0,
                this._specialStyles && this._specialStyles.start()),
                this.domPlayer.play()
            }
            pause() {
                this.init(),
                this.domPlayer.pause()
            }
            finish() {
                this.init(),
                this._specialStyles && this._specialStyles.finish(),
                this._onFinish(),
                this.domPlayer.finish()
            }
            reset() {
                this._resetDomPlayerState(),
                this._destroyed = !1,
                this._finished = !1,
                this._started = !1
            }
            _resetDomPlayerState() {
                this.domPlayer && this.domPlayer.cancel()
            }
            restart() {
                this.reset(),
                this.play()
            }
            hasStarted() {
                return this._started
            }
            destroy() {
                this._destroyed || (this._destroyed = !0,
                this._resetDomPlayerState(),
                this._onFinish(),
                this._specialStyles && this._specialStyles.destroy(),
                this._onDestroyFns.forEach(e=>e()),
                this._onDestroyFns = [])
            }
            setPosition(e) {
                void 0 === this.domPlayer && this.init(),
                this.domPlayer.currentTime = e * this.time
            }
            getPosition() {
                return this.domPlayer.currentTime / this.time
            }
            get totalTime() {
                return this._delay + this._duration
            }
            beforeDestroy() {
                const e = {};
                if (this.hasStarted()) {
                    const t = this._finalKeyframe;
                    Object.keys(t).forEach(r=>{
                        "offset" != r && (e[r] = this._finished ? t[r] : Qb(this.element, r))
                    }
                    )
                }
                this.currentSnapshot = e
            }
            triggerCallback(e) {
                const t = "start" == e ? this._onStartFns : this._onDoneFns;
                t.forEach(r=>r()),
                t.length = 0
            }
        }
        class Ek {
            validateStyleProperty(e) {
                return Bb(e)
            }
            matchesElement(e, t) {
                return !1
            }
            containsElement(e, t) {
                return jb(e, t)
            }
            getParentElement(e) {
                return Qd(e)
            }
            query(e, t, r) {
                return Hb(e, t, r)
            }
            computeStyle(e, t, r) {
                return window.getComputedStyle(e)[t]
            }
            animate(e, t, r, i, o, s=[]) {
                const l = {
                    duration: r,
                    delay: i,
                    fill: 0 == i ? "both" : "forwards"
                };
                o && (l.easing = o);
                const u = {}
                  , c = s.filter(f=>f instanceof cD);
                (function TO(n, e) {
                    return 0 === n || 0 === e
                }
                )(r, i) && c.forEach(f=>{
                    let h = f.currentSnapshot;
                    Object.keys(h).forEach(p=>u[p] = h[p])
                }
                ),
                t = function IO(n, e, t) {
                    const r = Object.keys(t);
                    if (r.length && e.length) {
                        let o = e[0]
                          , s = [];
                        if (r.forEach(a=>{
                            o.hasOwnProperty(a) || s.push(a),
                            o[a] = t[a]
                        }
                        ),
                        s.length)
                            for (var i = 1; i < e.length; i++) {
                                let a = e[i];
                                s.forEach(function(l) {
                                    a[l] = Qb(n, l)
                                })
                            }
                    }
                    return e
                }(e, t = t.map(f=>Qn(f, !1)), u);
                const d = function bk(n, e) {
                    let t = null
                      , r = null;
                    return Array.isArray(e) && e.length ? (t = pf(e[0]),
                    e.length > 1 && (r = pf(e[e.length - 1]))) : e && (t = pf(e)),
                    t || r ? new Dk(n,t,r) : null
                }(e, t);
                return new cD(e,t,l,d)
            }
        }
        let wk = (()=>{
            class n extends Sb {
                constructor(t, r) {
                    super(),
                    this._nextAnimationId = 0,
                    this._renderer = t.createRenderer(r.body, {
                        id: "0",
                        encapsulation: Gt.None,
                        styles: [],
                        data: {
                            animation: []
                        }
                    })
                }
                build(t) {
                    const r = this._nextAnimationId.toString();
                    this._nextAnimationId++;
                    const i = Array.isArray(t) ? xb(t) : t;
                    return dD(this._renderer, null, r, "register", [i]),
                    new Mk(r,this._renderer)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(po),w(ge))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        class Mk extends class k1 {
        }
        {
            constructor(e, t) {
                super(),
                this._id = e,
                this._renderer = t
            }
            create(e, t) {
                return new Ak(this._id,e,t || {},this._renderer)
            }
        }
        class Ak {
            constructor(e, t, r, i) {
                this.id = e,
                this.element = t,
                this._renderer = i,
                this.parentPlayer = null,
                this._started = !1,
                this.totalTime = 0,
                this._command("create", r)
            }
            _listen(e, t) {
                return this._renderer.listen(this.element, `@@${this.id}:${e}`, t)
            }
            _command(e, ...t) {
                return dD(this._renderer, this.element, this.id, e, t)
            }
            onDone(e) {
                this._listen("done", e)
            }
            onStart(e) {
                this._listen("start", e)
            }
            onDestroy(e) {
                this._listen("destroy", e)
            }
            init() {
                this._command("init")
            }
            hasStarted() {
                return this._started
            }
            play() {
                this._command("play"),
                this._started = !0
            }
            pause() {
                this._command("pause")
            }
            restart() {
                this._command("restart")
            }
            finish() {
                this._command("finish")
            }
            destroy() {
                this._command("destroy")
            }
            reset() {
                this._command("reset"),
                this._started = !1
            }
            setPosition(e) {
                this._command("setPosition", e)
            }
            getPosition() {
                var e, t;
                return null !== (t = null === (e = this._renderer.engine.players[+this.id]) || void 0 === e ? void 0 : e.getPosition()) && void 0 !== t ? t : 0
            }
        }
        function dD(n, e, t, r, i) {
            return n.setProperty(e, `@@${t}:${r}`, i)
        }
        const fD = "@.disabled";
        let Tk = (()=>{
            class n {
                constructor(t, r, i) {
                    this.delegate = t,
                    this.engine = r,
                    this._zone = i,
                    this._currentId = 0,
                    this._microtaskId = 1,
                    this._animationCallbacksBuffer = [],
                    this._rendererCache = new Map,
                    this._cdRecurDepth = 0,
                    this.promise = Promise.resolve(0),
                    r.onRemovalComplete = (o,s)=>{
                        const a = null == s ? void 0 : s.parentNode(o);
                        a && s.removeChild(a, o)
                    }
                }
                createRenderer(t, r) {
                    const o = this.delegate.createRenderer(t, r);
                    if (!(t && r && r.data && r.data.animation)) {
                        let c = this._rendererCache.get(o);
                        return c || (c = new hD("",o,this.engine),
                        this._rendererCache.set(o, c)),
                        c
                    }
                    const s = r.id
                      , a = r.id + "-" + this._currentId;
                    this._currentId++,
                    this.engine.register(a, t);
                    const l = c=>{
                        Array.isArray(c) ? c.forEach(l) : this.engine.registerTrigger(s, a, t, c.name, c)
                    }
                    ;
                    return r.data.animation.forEach(l),
                    new Ik(this,a,o,this.engine)
                }
                begin() {
                    this._cdRecurDepth++,
                    this.delegate.begin && this.delegate.begin()
                }
                _scheduleCountTask() {
                    this.promise.then(()=>{
                        this._microtaskId++
                    }
                    )
                }
                scheduleListenerCallback(t, r, i) {
                    t >= 0 && t < this._microtaskId ? this._zone.run(()=>r(i)) : (0 == this._animationCallbacksBuffer.length && Promise.resolve(null).then(()=>{
                        this._zone.run(()=>{
                            this._animationCallbacksBuffer.forEach(o=>{
                                const [s,a] = o;
                                s(a)
                            }
                            ),
                            this._animationCallbacksBuffer = []
                        }
                        )
                    }
                    ),
                    this._animationCallbacksBuffer.push([r, i]))
                }
                end() {
                    this._cdRecurDepth--,
                    0 == this._cdRecurDepth && this._zone.runOutsideAngular(()=>{
                        this._scheduleCountTask(),
                        this.engine.flush(this._microtaskId)
                    }
                    ),
                    this.delegate.end && this.delegate.end()
                }
                whenRenderingDone() {
                    return this.engine.whenRenderingDone()
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(po),w(Za),w(_e))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        class hD {
            constructor(e, t, r) {
                this.namespaceId = e,
                this.delegate = t,
                this.engine = r,
                this.destroyNode = this.delegate.destroyNode ? i=>t.destroyNode(i) : null
            }
            get data() {
                return this.delegate.data
            }
            destroy() {
                this.engine.destroy(this.namespaceId, this.delegate),
                this.delegate.destroy()
            }
            createElement(e, t) {
                return this.delegate.createElement(e, t)
            }
            createComment(e) {
                return this.delegate.createComment(e)
            }
            createText(e) {
                return this.delegate.createText(e)
            }
            appendChild(e, t) {
                this.delegate.appendChild(e, t),
                this.engine.onInsert(this.namespaceId, t, e, !1)
            }
            insertBefore(e, t, r, i=!0) {
                this.delegate.insertBefore(e, t, r),
                this.engine.onInsert(this.namespaceId, t, e, i)
            }
            removeChild(e, t, r) {
                this.engine.onRemove(this.namespaceId, t, this.delegate, r)
            }
            selectRootElement(e, t) {
                return this.delegate.selectRootElement(e, t)
            }
            parentNode(e) {
                return this.delegate.parentNode(e)
            }
            nextSibling(e) {
                return this.delegate.nextSibling(e)
            }
            setAttribute(e, t, r, i) {
                this.delegate.setAttribute(e, t, r, i)
            }
            removeAttribute(e, t, r) {
                this.delegate.removeAttribute(e, t, r)
            }
            addClass(e, t) {
                this.delegate.addClass(e, t)
            }
            removeClass(e, t) {
                this.delegate.removeClass(e, t)
            }
            setStyle(e, t, r, i) {
                this.delegate.setStyle(e, t, r, i)
            }
            removeStyle(e, t, r) {
                this.delegate.removeStyle(e, t, r)
            }
            setProperty(e, t, r) {
                "@" == t.charAt(0) && t == fD ? this.disableAnimations(e, !!r) : this.delegate.setProperty(e, t, r)
            }
            setValue(e, t) {
                this.delegate.setValue(e, t)
            }
            listen(e, t, r) {
                return this.delegate.listen(e, t, r)
            }
            disableAnimations(e, t) {
                this.engine.disableAnimations(e, t)
            }
        }
        class Ik extends hD {
            constructor(e, t, r, i) {
                super(t, r, i),
                this.factory = e,
                this.namespaceId = t
            }
            setProperty(e, t, r) {
                "@" == t.charAt(0) ? "." == t.charAt(1) && t == fD ? this.disableAnimations(e, r = void 0 === r || !!r) : this.engine.process(this.namespaceId, e, t.substr(1), r) : this.delegate.setProperty(e, t, r)
            }
            listen(e, t, r) {
                if ("@" == t.charAt(0)) {
                    const i = function Sk(n) {
                        switch (n) {
                        case "body":
                            return document.body;
                        case "document":
                            return document;
                        case "window":
                            return window;
                        default:
                            return n
                        }
                    }(e);
                    let o = t.substr(1)
                      , s = "";
                    return "@" != o.charAt(0) && ([o,s] = function xk(n) {
                        const e = n.indexOf(".");
                        return [n.substring(0, e), n.substr(e + 1)]
                    }(o)),
                    this.engine.listen(this.namespaceId, i, o, s, a=>{
                        this.factory.scheduleListenerCallback(a._data || -1, r, a)
                    }
                    )
                }
                return this.delegate.listen(e, t, r)
            }
        }
        let Fk = (()=>{
            class n extends Za {
                constructor(t, r, i) {
                    super(t.body, r, i)
                }
                ngOnDestroy() {
                    this.flush()
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(ge),w(Zd),w(lf))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac
            }),
            n
        }
        )();
        const wi = new S("AnimationModuleType")
          , pD = [{
            provide: Sb,
            useClass: wk
        }, {
            provide: lf,
            useFactory: function Nk() {
                return new ZO
            }
        }, {
            provide: Za,
            useClass: Fk
        }, {
            provide: po,
            useFactory: function Ok(n, e, t) {
                return new Tk(n,e,t)
            },
            deps: [ya, Za, _e]
        }]
          , mD = [{
            provide: Zd,
            useFactory: ()=>new Ek
        }, {
            provide: wi,
            useValue: "BrowserAnimations"
        }, ...pD]
          , kk = [{
            provide: Zd,
            useClass: Ub
        }, {
            provide: wi,
            useValue: "NoopAnimations"
        }, ...pD];
        let Rk = (()=>{
            class n {
                static withConfig(t) {
                    return {
                        ngModule: n,
                        providers: t.disableAnimations ? kk : mD
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                providers: mD,
                imports: [rv]
            }),
            n
        }
        )();
        const Pk = new S("cdk-dir-doc",{
            providedIn: "root",
            factory: function Lk() {
                return Ds(ge)
            }
        })
          , Vk = /^(ar|ckb|dv|he|iw|fa|nqo|ps|sd|ug|ur|yi|.*[-_](Adlm|Arab|Hebr|Nkoo|Rohg|Thaa))(?!.*[-_](Latn|Cyrl)($|-|_))($|-|_)/i;
        let mf, jk = (()=>{
            class n {
                constructor(t) {
                    if (this.value = "ltr",
                    this.change = new je,
                    t) {
                        const i = t.documentElement ? t.documentElement.dir : null;
                        this.value = function Bk(n) {
                            const e = (null == n ? void 0 : n.toLowerCase()) || "";
                            return "auto" === e && "undefined" != typeof navigator && (null == navigator ? void 0 : navigator.language) ? Vk.test(navigator.language) ? "rtl" : "ltr" : "rtl" === e ? "rtl" : "ltr"
                        }((t.body ? t.body.dir : null) || i || "ltr")
                    }
                }
                ngOnDestroy() {
                    this.change.complete()
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(Pk, 8))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )(), gD = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({}),
            n
        }
        )();
        try {
            mf = "undefined" != typeof Intl && Intl.v8BreakIterator
        } catch (n) {
            mf = !1
        }
        let Mi, Zn = (()=>{
            class n {
                constructor(t) {
                    this._platformId = t,
                    this.isBrowser = this._platformId ? function xF(n) {
                        return n === G_
                    }(this._platformId) : "object" == typeof document && !!document,
                    this.EDGE = this.isBrowser && /(edge)/i.test(navigator.userAgent),
                    this.TRIDENT = this.isBrowser && /(msie|trident)/i.test(navigator.userAgent),
                    this.BLINK = this.isBrowser && !(!window.chrome && !mf) && "undefined" != typeof CSS && !this.EDGE && !this.TRIDENT,
                    this.WEBKIT = this.isBrowser && /AppleWebKit/i.test(navigator.userAgent) && !this.BLINK && !this.EDGE && !this.TRIDENT,
                    this.IOS = this.isBrowser && /iPad|iPhone|iPod/.test(navigator.userAgent) && !("MSStream"in window),
                    this.FIREFOX = this.isBrowser && /(firefox|minefield)/i.test(navigator.userAgent),
                    this.ANDROID = this.isBrowser && /android/i.test(navigator.userAgent) && !this.TRIDENT,
                    this.SAFARI = this.isBrowser && /safari/i.test(navigator.userAgent) && this.WEBKIT
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(Xs))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        const _D = ["color", "button", "checkbox", "date", "datetime-local", "email", "file", "hidden", "image", "month", "number", "password", "radio", "range", "reset", "search", "submit", "tel", "text", "time", "url", "week"];
        function vD() {
            if (Mi)
                return Mi;
            if ("object" != typeof document || !document)
                return Mi = new Set(_D),
                Mi;
            let n = document.createElement("input");
            return Mi = new Set(_D.filter(e=>(n.setAttribute("type", e),
            n.type === e))),
            Mi
        }
        let Ro, gf;
        function Xa(n) {
            return function Hk() {
                if (null == Ro && "undefined" != typeof window)
                    try {
                        window.addEventListener("test", null, Object.defineProperty({}, "passive", {
                            get: ()=>Ro = !0
                        }))
                    } finally {
                        Ro = Ro || !1
                    }
                return Ro
            }() ? n : !!n.capture
        }
        function Po(n) {
            return n.composedPath ? n.composedPath()[0] : n.target
        }
        class zk extends Ut {
            constructor(e) {
                super(),
                this._value = e
            }
            get value() {
                return this.getValue()
            }
            _subscribe(e) {
                const t = super._subscribe(e);
                return !t.closed && e.next(this._value),
                t
            }
            getValue() {
                const {hasError: e, thrownError: t, _value: r} = this;
                if (e)
                    throw t;
                return this._throwIfClosed(),
                r
            }
            next(e) {
                super.next(this._value = e)
            }
        }
        function Jk(n, e) {
            return n === e
        }
        function el(n) {
            return st((e,t)=>{
                rn(n).subscribe(St(t, ()=>t.complete(), al)),
                !t.closed && e.subscribe(t)
            }
            )
        }
        function Yn(n) {
            return null != n && "false" != `${n}`
        }
        function Xn(n) {
            return n instanceof Pe ? n.nativeElement : n
        }
        function ED(n) {
            return 0 === n.buttons || 0 === n.offsetX && 0 === n.offsetY
        }
        function wD(n) {
            const e = n.touches && n.touches[0] || n.changedTouches && n.changedTouches[0];
            return !(!e || -1 !== e.identifier || null != e.radiusX && 1 !== e.radiusX || null != e.radiusY && 1 !== e.radiusY)
        }
        const uR = new S("cdk-input-modality-detector-options")
          , cR = {
            ignoreKeys: [18, 17, 224, 91, 16]
        }
          , Ai = Xa({
            passive: !0,
            capture: !0
        });
        let dR = (()=>{
            class n {
                constructor(t, r, i, o) {
                    this._platform = t,
                    this._mostRecentTarget = null,
                    this._modality = new zk(null),
                    this._lastTouchMs = 0,
                    this._onKeydown = s=>{
                        var a, l;
                        (null === (l = null === (a = this._options) || void 0 === a ? void 0 : a.ignoreKeys) || void 0 === l ? void 0 : l.some(u=>u === s.keyCode)) || (this._modality.next("keyboard"),
                        this._mostRecentTarget = Po(s))
                    }
                    ,
                    this._onMousedown = s=>{
                        Date.now() - this._lastTouchMs < 650 || (this._modality.next(ED(s) ? "keyboard" : "mouse"),
                        this._mostRecentTarget = Po(s))
                    }
                    ,
                    this._onTouchstart = s=>{
                        wD(s) ? this._modality.next("keyboard") : (this._lastTouchMs = Date.now(),
                        this._modality.next("touch"),
                        this._mostRecentTarget = Po(s))
                    }
                    ,
                    this._options = Object.assign(Object.assign({}, cR), o),
                    this.modalityDetected = this._modality.pipe(function Yk(n) {
                        return av((e,t)=>n <= t)
                    }(1)),
                    this.modalityChanged = this.modalityDetected.pipe(function Xk(n, e=qo) {
                        return n = null != n ? n : Jk,
                        st((t,r)=>{
                            let i, o = !0;
                            t.subscribe(St(r, s=>{
                                const a = e(s);
                                (o || !n(i, a)) && (o = !1,
                                i = a,
                                r.next(s))
                            }
                            ))
                        }
                        )
                    }()),
                    t.isBrowser && r.runOutsideAngular(()=>{
                        i.addEventListener("keydown", this._onKeydown, Ai),
                        i.addEventListener("mousedown", this._onMousedown, Ai),
                        i.addEventListener("touchstart", this._onTouchstart, Ai)
                    }
                    )
                }
                get mostRecentModality() {
                    return this._modality.value
                }
                ngOnDestroy() {
                    this._modality.complete(),
                    this._platform.isBrowser && (document.removeEventListener("keydown", this._onKeydown, Ai),
                    document.removeEventListener("mousedown", this._onMousedown, Ai),
                    document.removeEventListener("touchstart", this._onTouchstart, Ai))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(Zn),w(_e),w(ge),w(uR, 8))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        const hR = new S("cdk-focus-monitor-default-options")
          , tl = Xa({
            passive: !0,
            capture: !0
        });
        let pR = (()=>{
            class n {
                constructor(t, r, i, o, s) {
                    this._ngZone = t,
                    this._platform = r,
                    this._inputModalityDetector = i,
                    this._origin = null,
                    this._windowFocused = !1,
                    this._originFromTouchInteraction = !1,
                    this._elementInfo = new Map,
                    this._monitoredElementCount = 0,
                    this._rootNodeFocusListenerCount = new Map,
                    this._windowFocusListener = ()=>{
                        this._windowFocused = !0,
                        this._windowFocusTimeoutId = window.setTimeout(()=>this._windowFocused = !1)
                    }
                    ,
                    this._stopInputModalityDetector = new Ut,
                    this._rootNodeFocusAndBlurListener = a=>{
                        const l = Po(a)
                          , u = "focus" === a.type ? this._onFocus : this._onBlur;
                        for (let c = l; c; c = c.parentElement)
                            u.call(this, a, c)
                    }
                    ,
                    this._document = o,
                    this._detectionMode = (null == s ? void 0 : s.detectionMode) || 0
                }
                monitor(t, r=!1) {
                    const i = Xn(t);
                    if (!this._platform.isBrowser || 1 !== i.nodeType)
                        return br(null);
                    const o = function $k(n) {
                        if (function Uk() {
                            if (null == gf) {
                                const n = "undefined" != typeof document ? document.head : null;
                                gf = !(!n || !n.createShadowRoot && !n.attachShadow)
                            }
                            return gf
                        }()) {
                            const e = n.getRootNode ? n.getRootNode() : null;
                            if ("undefined" != typeof ShadowRoot && ShadowRoot && e instanceof ShadowRoot)
                                return e
                        }
                        return null
                    }(i) || this._getDocument()
                      , s = this._elementInfo.get(i);
                    if (s)
                        return r && (s.checkChildren = !0),
                        s.subject;
                    const a = {
                        checkChildren: r,
                        subject: new Ut,
                        rootNode: o
                    };
                    return this._elementInfo.set(i, a),
                    this._registerGlobalListeners(a),
                    a.subject
                }
                stopMonitoring(t) {
                    const r = Xn(t)
                      , i = this._elementInfo.get(r);
                    i && (i.subject.complete(),
                    this._setClasses(r),
                    this._elementInfo.delete(r),
                    this._removeGlobalListeners(i))
                }
                focusVia(t, r, i) {
                    const o = Xn(t);
                    o === this._getDocument().activeElement ? this._getClosestElementsInfo(o).forEach(([a,l])=>this._originChanged(a, r, l)) : (this._setOrigin(r),
                    "function" == typeof o.focus && o.focus(i))
                }
                ngOnDestroy() {
                    this._elementInfo.forEach((t,r)=>this.stopMonitoring(r))
                }
                _getDocument() {
                    return this._document || document
                }
                _getWindow() {
                    return this._getDocument().defaultView || window
                }
                _getFocusOrigin(t) {
                    return this._origin ? this._originFromTouchInteraction ? this._shouldBeAttributedToTouch(t) ? "touch" : "program" : this._origin : this._windowFocused && this._lastFocusOrigin ? this._lastFocusOrigin : "program"
                }
                _shouldBeAttributedToTouch(t) {
                    return 1 === this._detectionMode || !!(null == t ? void 0 : t.contains(this._inputModalityDetector._mostRecentTarget))
                }
                _setClasses(t, r) {
                    t.classList.toggle("cdk-focused", !!r),
                    t.classList.toggle("cdk-touch-focused", "touch" === r),
                    t.classList.toggle("cdk-keyboard-focused", "keyboard" === r),
                    t.classList.toggle("cdk-mouse-focused", "mouse" === r),
                    t.classList.toggle("cdk-program-focused", "program" === r)
                }
                _setOrigin(t, r=!1) {
                    this._ngZone.runOutsideAngular(()=>{
                        this._origin = t,
                        this._originFromTouchInteraction = "touch" === t && r,
                        0 === this._detectionMode && (clearTimeout(this._originTimeoutId),
                        this._originTimeoutId = setTimeout(()=>this._origin = null, this._originFromTouchInteraction ? 650 : 1))
                    }
                    )
                }
                _onFocus(t, r) {
                    const i = this._elementInfo.get(r)
                      , o = Po(t);
                    !i || !i.checkChildren && r !== o || this._originChanged(r, this._getFocusOrigin(o), i)
                }
                _onBlur(t, r) {
                    const i = this._elementInfo.get(r);
                    !i || i.checkChildren && t.relatedTarget instanceof Node && r.contains(t.relatedTarget) || (this._setClasses(r),
                    this._emitOrigin(i.subject, null))
                }
                _emitOrigin(t, r) {
                    this._ngZone.run(()=>t.next(r))
                }
                _registerGlobalListeners(t) {
                    if (!this._platform.isBrowser)
                        return;
                    const r = t.rootNode
                      , i = this._rootNodeFocusListenerCount.get(r) || 0;
                    i || this._ngZone.runOutsideAngular(()=>{
                        r.addEventListener("focus", this._rootNodeFocusAndBlurListener, tl),
                        r.addEventListener("blur", this._rootNodeFocusAndBlurListener, tl)
                    }
                    ),
                    this._rootNodeFocusListenerCount.set(r, i + 1),
                    1 == ++this._monitoredElementCount && (this._ngZone.runOutsideAngular(()=>{
                        this._getWindow().addEventListener("focus", this._windowFocusListener)
                    }
                    ),
                    this._inputModalityDetector.modalityDetected.pipe(el(this._stopInputModalityDetector)).subscribe(o=>{
                        this._setOrigin(o, !0)
                    }
                    ))
                }
                _removeGlobalListeners(t) {
                    const r = t.rootNode;
                    if (this._rootNodeFocusListenerCount.has(r)) {
                        const i = this._rootNodeFocusListenerCount.get(r);
                        i > 1 ? this._rootNodeFocusListenerCount.set(r, i - 1) : (r.removeEventListener("focus", this._rootNodeFocusAndBlurListener, tl),
                        r.removeEventListener("blur", this._rootNodeFocusAndBlurListener, tl),
                        this._rootNodeFocusListenerCount.delete(r))
                    }
                    --this._monitoredElementCount || (this._getWindow().removeEventListener("focus", this._windowFocusListener),
                    this._stopInputModalityDetector.next(),
                    clearTimeout(this._windowFocusTimeoutId),
                    clearTimeout(this._originTimeoutId))
                }
                _originChanged(t, r, i) {
                    this._setClasses(t, r),
                    this._emitOrigin(i.subject, r),
                    this._lastFocusOrigin = r
                }
                _getClosestElementsInfo(t) {
                    const r = [];
                    return this._elementInfo.forEach((i,o)=>{
                        (o === t || i.checkChildren && o.contains(t)) && r.push([o, i])
                    }
                    ),
                    r
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(_e),w(Zn),w(dR),w(ge, 8),w(hR, 8))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        const AD = "cdk-high-contrast-black-on-white"
          , TD = "cdk-high-contrast-white-on-black"
          , yf = "cdk-high-contrast-active";
        let mR = (()=>{
            class n {
                constructor(t, r) {
                    this._platform = t,
                    this._document = r
                }
                getHighContrastMode() {
                    if (!this._platform.isBrowser)
                        return 0;
                    const t = this._document.createElement("div");
                    t.style.backgroundColor = "rgb(1,2,3)",
                    t.style.position = "absolute",
                    this._document.body.appendChild(t);
                    const r = this._document.defaultView || window
                      , i = r && r.getComputedStyle ? r.getComputedStyle(t) : null
                      , o = (i && i.backgroundColor || "").replace(/ /g, "");
                    switch (t.remove(),
                    o) {
                    case "rgb(0,0,0)":
                        return 2;
                    case "rgb(255,255,255)":
                        return 1
                    }
                    return 0
                }
                _applyBodyHighContrastModeCssClasses() {
                    if (!this._hasCheckedHighContrastMode && this._platform.isBrowser && this._document.body) {
                        const t = this._document.body.classList;
                        t.remove(yf),
                        t.remove(AD),
                        t.remove(TD),
                        this._hasCheckedHighContrastMode = !0;
                        const r = this.getHighContrastMode();
                        1 === r ? (t.add(yf),
                        t.add(AD)) : 2 === r && (t.add(yf),
                        t.add(TD))
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(Zn),w(ge))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        const yR = new S("mat-sanity-checks",{
            providedIn: "root",
            factory: function gR() {
                return !0
            }
        });
        let Et = (()=>{
            class n {
                constructor(t, r, i) {
                    this._sanityChecks = r,
                    this._document = i,
                    this._hasDoneGlobalChecks = !1,
                    t._applyBodyHighContrastModeCssClasses(),
                    this._hasDoneGlobalChecks || (this._hasDoneGlobalChecks = !0)
                }
                _checkIsEnabled(t) {
                    return !function Gk() {
                        return "undefined" != typeof __karma__ && !!__karma__ || "undefined" != typeof jasmine && !!jasmine || "undefined" != typeof jest && !!jest || "undefined" != typeof Mocha && !!Mocha
                    }() && ("boolean" == typeof this._sanityChecks ? this._sanityChecks : !!this._sanityChecks[t])
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(mR),w(yR, 8),w(ge))
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[gD], gD]
            }),
            n
        }
        )();
        function _R(n) {
            return class extends n {
                constructor(...e) {
                    super(...e),
                    this._disabled = !1
                }
                get disabled() {
                    return this._disabled
                }
                set disabled(e) {
                    this._disabled = Yn(e)
                }
            }
        }
        function nl(n, e) {
            return class extends n {
                constructor(...t) {
                    super(...t),
                    this.defaultColor = e,
                    this.color = e
                }
                get color() {
                    return this._color
                }
                set color(t) {
                    const r = t || this.defaultColor;
                    r !== this._color && (this._color && this._elementRef.nativeElement.classList.remove(`mat-${this._color}`),
                    r && this._elementRef.nativeElement.classList.add(`mat-${r}`),
                    this._color = r)
                }
            }
        }
        function vR(n) {
            return class extends n {
                constructor(...e) {
                    super(...e),
                    this._disableRipple = !1
                }
                get disableRipple() {
                    return this._disableRipple
                }
                set disableRipple(e) {
                    this._disableRipple = Yn(e)
                }
            }
        }
        function bR(n) {
            return class extends n {
                constructor(...e) {
                    super(...e),
                    this.stateChanges = new Ut,
                    this.errorState = !1
                }
                updateErrorState() {
                    const e = this.errorState
                      , o = (this.errorStateMatcher || this._defaultErrorStateMatcher).isErrorState(this.ngControl ? this.ngControl.control : null, this._parentFormGroup || this._parentForm);
                    o !== e && (this.errorState = o,
                    this.stateChanges.next())
                }
            }
        }
        let SD = (()=>{
            class n {
                isErrorState(t, r) {
                    return !!(t && t.invalid && (t.touched || r && r.submitted))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        class CR {
            constructor(e, t, r) {
                this._renderer = e,
                this.element = t,
                this.config = r,
                this.state = 3
            }
            fadeOut() {
                this._renderer.fadeOutRipple(this)
            }
        }
        const xD = {
            enterDuration: 225,
            exitDuration: 150
        }
          , _f = Xa({
            passive: !0
        })
          , FD = ["mousedown", "touchstart"]
          , ND = ["mouseup", "mouseleave", "touchend", "touchcancel"];
        class wR {
            constructor(e, t, r, i) {
                this._target = e,
                this._ngZone = t,
                this._isPointerDown = !1,
                this._activeRipples = new Set,
                this._pointerUpEventsRegistered = !1,
                i.isBrowser && (this._containerElement = Xn(r))
            }
            fadeInRipple(e, t, r={}) {
                const i = this._containerRect = this._containerRect || this._containerElement.getBoundingClientRect()
                  , o = Object.assign(Object.assign({}, xD), r.animation);
                r.centered && (e = i.left + i.width / 2,
                t = i.top + i.height / 2);
                const s = r.radius || function AR(n, e, t) {
                    const r = Math.max(Math.abs(n - t.left), Math.abs(n - t.right))
                      , i = Math.max(Math.abs(e - t.top), Math.abs(e - t.bottom));
                    return Math.sqrt(r * r + i * i)
                }(e, t, i)
                  , a = e - i.left
                  , l = t - i.top
                  , u = o.enterDuration
                  , c = document.createElement("div");
                c.classList.add("mat-ripple-element"),
                c.style.left = a - s + "px",
                c.style.top = l - s + "px",
                c.style.height = 2 * s + "px",
                c.style.width = 2 * s + "px",
                null != r.color && (c.style.backgroundColor = r.color),
                c.style.transitionDuration = `${u}ms`,
                this._containerElement.appendChild(c),
                function MR(n) {
                    window.getComputedStyle(n).getPropertyValue("opacity")
                }(c),
                c.style.transform = "scale(1)";
                const d = new CR(this,c,r);
                return d.state = 0,
                this._activeRipples.add(d),
                r.persistent || (this._mostRecentTransientRipple = d),
                this._runTimeoutOutsideZone(()=>{
                    const f = d === this._mostRecentTransientRipple;
                    d.state = 1,
                    !r.persistent && (!f || !this._isPointerDown) && d.fadeOut()
                }
                , u),
                d
            }
            fadeOutRipple(e) {
                const t = this._activeRipples.delete(e);
                if (e === this._mostRecentTransientRipple && (this._mostRecentTransientRipple = null),
                this._activeRipples.size || (this._containerRect = null),
                !t)
                    return;
                const r = e.element
                  , i = Object.assign(Object.assign({}, xD), e.config.animation);
                r.style.transitionDuration = `${i.exitDuration}ms`,
                r.style.opacity = "0",
                e.state = 2,
                this._runTimeoutOutsideZone(()=>{
                    e.state = 3,
                    r.remove()
                }
                , i.exitDuration)
            }
            fadeOutAll() {
                this._activeRipples.forEach(e=>e.fadeOut())
            }
            fadeOutAllNonPersistent() {
                this._activeRipples.forEach(e=>{
                    e.config.persistent || e.fadeOut()
                }
                )
            }
            setupTriggerEvents(e) {
                const t = Xn(e);
                !t || t === this._triggerElement || (this._removeTriggerEvents(),
                this._triggerElement = t,
                this._registerEvents(FD))
            }
            handleEvent(e) {
                "mousedown" === e.type ? this._onMousedown(e) : "touchstart" === e.type ? this._onTouchStart(e) : this._onPointerUp(),
                this._pointerUpEventsRegistered || (this._registerEvents(ND),
                this._pointerUpEventsRegistered = !0)
            }
            _onMousedown(e) {
                const t = ED(e)
                  , r = this._lastTouchStartEvent && Date.now() < this._lastTouchStartEvent + 800;
                !this._target.rippleDisabled && !t && !r && (this._isPointerDown = !0,
                this.fadeInRipple(e.clientX, e.clientY, this._target.rippleConfig))
            }
            _onTouchStart(e) {
                if (!this._target.rippleDisabled && !wD(e)) {
                    this._lastTouchStartEvent = Date.now(),
                    this._isPointerDown = !0;
                    const t = e.changedTouches;
                    for (let r = 0; r < t.length; r++)
                        this.fadeInRipple(t[r].clientX, t[r].clientY, this._target.rippleConfig)
                }
            }
            _onPointerUp() {
                !this._isPointerDown || (this._isPointerDown = !1,
                this._activeRipples.forEach(e=>{
                    !e.config.persistent && (1 === e.state || e.config.terminateOnPointerUp && 0 === e.state) && e.fadeOut()
                }
                ))
            }
            _runTimeoutOutsideZone(e, t=0) {
                this._ngZone.runOutsideAngular(()=>setTimeout(e, t))
            }
            _registerEvents(e) {
                this._ngZone.runOutsideAngular(()=>{
                    e.forEach(t=>{
                        this._triggerElement.addEventListener(t, this, _f)
                    }
                    )
                }
                )
            }
            _removeTriggerEvents() {
                this._triggerElement && (FD.forEach(e=>{
                    this._triggerElement.removeEventListener(e, this, _f)
                }
                ),
                this._pointerUpEventsRegistered && ND.forEach(e=>{
                    this._triggerElement.removeEventListener(e, this, _f)
                }
                ))
            }
        }
        const TR = new S("mat-ripple-global-options");
        let OD = (()=>{
            class n {
                constructor(t, r, i, o, s) {
                    this._elementRef = t,
                    this._animationMode = s,
                    this.radius = 0,
                    this._disabled = !1,
                    this._isInitialized = !1,
                    this._globalOptions = o || {},
                    this._rippleRenderer = new wR(this,r,t,i)
                }
                get disabled() {
                    return this._disabled
                }
                set disabled(t) {
                    t && this.fadeOutAllNonPersistent(),
                    this._disabled = t,
                    this._setupTriggerEventsIfEnabled()
                }
                get trigger() {
                    return this._trigger || this._elementRef.nativeElement
                }
                set trigger(t) {
                    this._trigger = t,
                    this._setupTriggerEventsIfEnabled()
                }
                ngOnInit() {
                    this._isInitialized = !0,
                    this._setupTriggerEventsIfEnabled()
                }
                ngOnDestroy() {
                    this._rippleRenderer._removeTriggerEvents()
                }
                fadeOutAll() {
                    this._rippleRenderer.fadeOutAll()
                }
                fadeOutAllNonPersistent() {
                    this._rippleRenderer.fadeOutAllNonPersistent()
                }
                get rippleConfig() {
                    return {
                        centered: this.centered,
                        radius: this.radius,
                        color: this.color,
                        animation: Object.assign(Object.assign(Object.assign({}, this._globalOptions.animation), "NoopAnimations" === this._animationMode ? {
                            enterDuration: 0,
                            exitDuration: 0
                        } : {}), this.animation),
                        terminateOnPointerUp: this._globalOptions.terminateOnPointerUp
                    }
                }
                get rippleDisabled() {
                    return this.disabled || !!this._globalOptions.disabled
                }
                _setupTriggerEventsIfEnabled() {
                    !this.disabled && this._isInitialized && this._rippleRenderer.setupTriggerEvents(this.trigger)
                }
                launch(t, r=0, i) {
                    return "number" == typeof t ? this._rippleRenderer.fadeInRipple(t, r, Object.assign(Object.assign({}, this.rippleConfig), i)) : this._rippleRenderer.fadeInRipple(0, 0, Object.assign(Object.assign({}, this.rippleConfig), t))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Pe),v(_e),v(Zn),v(TR, 8),v(wi, 8))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "mat-ripple", ""], ["", "matRipple", ""]],
                hostAttrs: [1, "mat-ripple"],
                hostVars: 2,
                hostBindings: function(t, r) {
                    2 & t && Je("mat-ripple-unbounded", r.unbounded)
                },
                inputs: {
                    color: ["matRippleColor", "color"],
                    unbounded: ["matRippleUnbounded", "unbounded"],
                    centered: ["matRippleCentered", "centered"],
                    radius: ["matRippleRadius", "radius"],
                    animation: ["matRippleAnimation", "animation"],
                    disabled: ["matRippleDisabled", "disabled"],
                    trigger: ["matRippleTrigger", "trigger"]
                },
                exportAs: ["matRipple"]
            }),
            n
        }
        )()
          , IR = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[Et], Et]
            }),
            n
        }
        )();
        const SR = ["mat-button", ""]
          , xR = ["*"]
          , NR = ["mat-button", "mat-flat-button", "mat-icon-button", "mat-raised-button", "mat-stroked-button", "mat-mini-fab", "mat-fab"]
          , OR = nl(_R(vR(class {
            constructor(n) {
                this._elementRef = n
            }
        }
        )));
        let kD = (()=>{
            class n extends OR {
                constructor(t, r, i) {
                    super(t),
                    this._focusMonitor = r,
                    this._animationMode = i,
                    this.isRoundButton = this._hasHostAttributes("mat-fab", "mat-mini-fab"),
                    this.isIconButton = this._hasHostAttributes("mat-icon-button");
                    for (const o of NR)
                        this._hasHostAttributes(o) && this._getHostElement().classList.add(o);
                    t.nativeElement.classList.add("mat-button-base"),
                    this.isRoundButton && (this.color = "accent")
                }
                ngAfterViewInit() {
                    this._focusMonitor.monitor(this._elementRef, !0)
                }
                ngOnDestroy() {
                    this._focusMonitor.stopMonitoring(this._elementRef)
                }
                focus(t, r) {
                    t ? this._focusMonitor.focusVia(this._getHostElement(), t, r) : this._getHostElement().focus(r)
                }
                _getHostElement() {
                    return this._elementRef.nativeElement
                }
                _isRippleDisabled() {
                    return this.disableRipple || this.disabled
                }
                _hasHostAttributes(...t) {
                    return t.some(r=>this._getHostElement().hasAttribute(r))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Pe),v(pR),v(wi, 8))
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["button", "mat-button", ""], ["button", "mat-raised-button", ""], ["button", "mat-icon-button", ""], ["button", "mat-fab", ""], ["button", "mat-mini-fab", ""], ["button", "mat-stroked-button", ""], ["button", "mat-flat-button", ""]],
                viewQuery: function(t, r) {
                    if (1 & t && _o(OD, 5),
                    2 & t) {
                        let i;
                        tt(i = nt()) && (r.ripple = i.first)
                    }
                },
                hostAttrs: [1, "mat-focus-indicator"],
                hostVars: 5,
                hostBindings: function(t, r) {
                    2 & t && (bt("disabled", r.disabled || null),
                    Je("_mat-animation-noopable", "NoopAnimations" === r._animationMode)("mat-button-disabled", r.disabled))
                },
                inputs: {
                    disabled: "disabled",
                    disableRipple: "disableRipple",
                    color: "color"
                },
                exportAs: ["matButton"],
                features: [Y],
                attrs: SR,
                ngContentSelectors: xR,
                decls: 4,
                vars: 5,
                consts: [[1, "mat-button-wrapper"], ["matRipple", "", 1, "mat-button-ripple", 3, "matRippleDisabled", "matRippleCentered", "matRippleTrigger"], [1, "mat-button-focus-overlay"]],
                template: function(t, r) {
                    1 & t && (hr(),
                    B(0, "span", 0),
                    Be(1),
                    j(),
                    ke(2, "span", 1)(3, "span", 2)),
                    2 & t && (de(2),
                    Je("mat-button-ripple-round", r.isRoundButton || r.isIconButton),
                    fe("matRippleDisabled", r._isRippleDisabled())("matRippleCentered", r.isIconButton)("matRippleTrigger", r._getHostElement()))
                },
                directives: [OD],
                styles: [".mat-button .mat-button-focus-overlay,.mat-icon-button .mat-button-focus-overlay{opacity:0}.mat-button:hover:not(.mat-button-disabled) .mat-button-focus-overlay,.mat-stroked-button:hover:not(.mat-button-disabled) .mat-button-focus-overlay{opacity:.04}@media(hover: none){.mat-button:hover:not(.mat-button-disabled) .mat-button-focus-overlay,.mat-stroked-button:hover:not(.mat-button-disabled) .mat-button-focus-overlay{opacity:0}}.mat-button,.mat-icon-button,.mat-stroked-button,.mat-flat-button{box-sizing:border-box;position:relative;-webkit-user-select:none;user-select:none;cursor:pointer;outline:none;border:none;-webkit-tap-highlight-color:transparent;display:inline-block;white-space:nowrap;text-decoration:none;vertical-align:baseline;text-align:center;margin:0;min-width:64px;line-height:36px;padding:0 16px;border-radius:4px;overflow:visible}.mat-button::-moz-focus-inner,.mat-icon-button::-moz-focus-inner,.mat-stroked-button::-moz-focus-inner,.mat-flat-button::-moz-focus-inner{border:0}.mat-button.mat-button-disabled,.mat-icon-button.mat-button-disabled,.mat-stroked-button.mat-button-disabled,.mat-flat-button.mat-button-disabled{cursor:default}.mat-button.cdk-keyboard-focused .mat-button-focus-overlay,.mat-button.cdk-program-focused .mat-button-focus-overlay,.mat-icon-button.cdk-keyboard-focused .mat-button-focus-overlay,.mat-icon-button.cdk-program-focused .mat-button-focus-overlay,.mat-stroked-button.cdk-keyboard-focused .mat-button-focus-overlay,.mat-stroked-button.cdk-program-focused .mat-button-focus-overlay,.mat-flat-button.cdk-keyboard-focused .mat-button-focus-overlay,.mat-flat-button.cdk-program-focused .mat-button-focus-overlay{opacity:.12}.mat-button::-moz-focus-inner,.mat-icon-button::-moz-focus-inner,.mat-stroked-button::-moz-focus-inner,.mat-flat-button::-moz-focus-inner{border:0}.mat-raised-button{box-sizing:border-box;position:relative;-webkit-user-select:none;user-select:none;cursor:pointer;outline:none;border:none;-webkit-tap-highlight-color:transparent;display:inline-block;white-space:nowrap;text-decoration:none;vertical-align:baseline;text-align:center;margin:0;min-width:64px;line-height:36px;padding:0 16px;border-radius:4px;overflow:visible;transform:translate3d(0, 0, 0);transition:background 400ms cubic-bezier(0.25, 0.8, 0.25, 1),box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1)}.mat-raised-button::-moz-focus-inner{border:0}.mat-raised-button.mat-button-disabled{cursor:default}.mat-raised-button.cdk-keyboard-focused .mat-button-focus-overlay,.mat-raised-button.cdk-program-focused .mat-button-focus-overlay{opacity:.12}.mat-raised-button::-moz-focus-inner{border:0}._mat-animation-noopable.mat-raised-button{transition:none;animation:none}.mat-stroked-button{border:1px solid currentColor;padding:0 15px;line-height:34px}.mat-stroked-button .mat-button-ripple.mat-ripple,.mat-stroked-button .mat-button-focus-overlay{top:-1px;left:-1px;right:-1px;bottom:-1px}.mat-fab{box-sizing:border-box;position:relative;-webkit-user-select:none;user-select:none;cursor:pointer;outline:none;border:none;-webkit-tap-highlight-color:transparent;display:inline-block;white-space:nowrap;text-decoration:none;vertical-align:baseline;text-align:center;margin:0;min-width:64px;line-height:36px;padding:0 16px;border-radius:4px;overflow:visible;transform:translate3d(0, 0, 0);transition:background 400ms cubic-bezier(0.25, 0.8, 0.25, 1),box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1);min-width:0;border-radius:50%;width:56px;height:56px;padding:0;flex-shrink:0}.mat-fab::-moz-focus-inner{border:0}.mat-fab.mat-button-disabled{cursor:default}.mat-fab.cdk-keyboard-focused .mat-button-focus-overlay,.mat-fab.cdk-program-focused .mat-button-focus-overlay{opacity:.12}.mat-fab::-moz-focus-inner{border:0}._mat-animation-noopable.mat-fab{transition:none;animation:none}.mat-fab .mat-button-wrapper{padding:16px 0;display:inline-block;line-height:24px}.mat-mini-fab{box-sizing:border-box;position:relative;-webkit-user-select:none;user-select:none;cursor:pointer;outline:none;border:none;-webkit-tap-highlight-color:transparent;display:inline-block;white-space:nowrap;text-decoration:none;vertical-align:baseline;text-align:center;margin:0;min-width:64px;line-height:36px;padding:0 16px;border-radius:4px;overflow:visible;transform:translate3d(0, 0, 0);transition:background 400ms cubic-bezier(0.25, 0.8, 0.25, 1),box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1);min-width:0;border-radius:50%;width:40px;height:40px;padding:0;flex-shrink:0}.mat-mini-fab::-moz-focus-inner{border:0}.mat-mini-fab.mat-button-disabled{cursor:default}.mat-mini-fab.cdk-keyboard-focused .mat-button-focus-overlay,.mat-mini-fab.cdk-program-focused .mat-button-focus-overlay{opacity:.12}.mat-mini-fab::-moz-focus-inner{border:0}._mat-animation-noopable.mat-mini-fab{transition:none;animation:none}.mat-mini-fab .mat-button-wrapper{padding:8px 0;display:inline-block;line-height:24px}.mat-icon-button{padding:0;min-width:0;width:40px;height:40px;flex-shrink:0;line-height:40px;border-radius:50%}.mat-icon-button i,.mat-icon-button .mat-icon{line-height:24px}.mat-button-ripple.mat-ripple,.mat-button-focus-overlay{top:0;left:0;right:0;bottom:0;position:absolute;pointer-events:none;border-radius:inherit}.mat-button-ripple.mat-ripple:not(:empty){transform:translateZ(0)}.mat-button-focus-overlay{opacity:0;transition:opacity 200ms cubic-bezier(0.35, 0, 0.25, 1),background-color 200ms cubic-bezier(0.35, 0, 0.25, 1)}._mat-animation-noopable .mat-button-focus-overlay{transition:none}.mat-button-ripple-round{border-radius:50%;z-index:1}.mat-button .mat-button-wrapper>*,.mat-flat-button .mat-button-wrapper>*,.mat-stroked-button .mat-button-wrapper>*,.mat-raised-button .mat-button-wrapper>*,.mat-icon-button .mat-button-wrapper>*,.mat-fab .mat-button-wrapper>*,.mat-mini-fab .mat-button-wrapper>*{vertical-align:middle}.mat-form-field:not(.mat-form-field-appearance-legacy) .mat-form-field-prefix .mat-icon-button,.mat-form-field:not(.mat-form-field-appearance-legacy) .mat-form-field-suffix .mat-icon-button{display:inline-flex;justify-content:center;align-items:center;font-size:inherit;width:2.5em;height:2.5em}.cdk-high-contrast-active .mat-button,.cdk-high-contrast-active .mat-flat-button,.cdk-high-contrast-active .mat-raised-button,.cdk-high-contrast-active .mat-icon-button,.cdk-high-contrast-active .mat-fab,.cdk-high-contrast-active .mat-mini-fab{outline:solid 1px}.cdk-high-contrast-active .mat-button-base.cdk-keyboard-focused,.cdk-high-contrast-active .mat-button-base.cdk-program-focused{outline:solid 3px}\n"],
                encapsulation: 2,
                changeDetection: 0
            }),
            n
        }
        )()
          , kR = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[IR, Et], Et]
            }),
            n
        }
        )();
        const RR = ["*", [["mat-card-footer"]]]
          , PR = ["*", "mat-card-footer"]
          , LR = [[["", "mat-card-avatar", ""], ["", "matCardAvatar", ""]], [["mat-card-title"], ["mat-card-subtitle"], ["", "mat-card-title", ""], ["", "mat-card-subtitle", ""], ["", "matCardTitle", ""], ["", "matCardSubtitle", ""]], "*"]
          , VR = ["[mat-card-avatar], [matCardAvatar]", "mat-card-title, mat-card-subtitle,\n      [mat-card-title], [mat-card-subtitle],\n      [matCardTitle], [matCardSubtitle]", "*"];
        let BR = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["mat-card-content"], ["", "mat-card-content", ""], ["", "matCardContent", ""]],
                hostAttrs: [1, "mat-card-content"]
            }),
            n
        }
        )()
          , RD = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["mat-card-title"], ["", "mat-card-title", ""], ["", "matCardTitle", ""]],
                hostAttrs: [1, "mat-card-title"]
            }),
            n
        }
        )()
          , jR = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["mat-card-subtitle"], ["", "mat-card-subtitle", ""], ["", "matCardSubtitle", ""]],
                hostAttrs: [1, "mat-card-subtitle"]
            }),
            n
        }
        )()
          , HR = (()=>{
            class n {
                constructor() {
                    this.align = "start"
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["mat-card-actions"]],
                hostAttrs: [1, "mat-card-actions"],
                hostVars: 2,
                hostBindings: function(t, r) {
                    2 & t && Je("mat-card-actions-align-end", "end" === r.align)
                },
                inputs: {
                    align: "align"
                },
                exportAs: ["matCardActions"]
            }),
            n
        }
        )()
          , UR = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "mat-card-image", ""], ["", "matCardImage", ""]],
                hostAttrs: [1, "mat-card-image"]
            }),
            n
        }
        )()
          , PD = (()=>{
            class n {
                constructor(t) {
                    this._animationMode = t
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(wi, 8))
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["mat-card"]],
                hostAttrs: [1, "mat-card", "mat-focus-indicator"],
                hostVars: 2,
                hostBindings: function(t, r) {
                    2 & t && Je("_mat-animation-noopable", "NoopAnimations" === r._animationMode)
                },
                exportAs: ["matCard"],
                ngContentSelectors: PR,
                decls: 2,
                vars: 0,
                template: function(t, r) {
                    1 & t && (hr(RR),
                    Be(0),
                    Be(1, 1))
                },
                styles: [".mat-card{transition:box-shadow 280ms cubic-bezier(0.4, 0, 0.2, 1);display:block;position:relative;padding:16px;border-radius:4px}._mat-animation-noopable.mat-card{transition:none;animation:none}.mat-card .mat-divider-horizontal{position:absolute;left:0;width:100%}[dir=rtl] .mat-card .mat-divider-horizontal{left:auto;right:0}.mat-card .mat-divider-horizontal.mat-divider-inset{position:static;margin:0}[dir=rtl] .mat-card .mat-divider-horizontal.mat-divider-inset{margin-right:0}.cdk-high-contrast-active .mat-card{outline:solid 1px}.mat-card-actions,.mat-card-subtitle,.mat-card-content{display:block;margin-bottom:16px}.mat-card-title{display:block;margin-bottom:8px}.mat-card-actions{margin-left:-8px;margin-right:-8px;padding:8px 0}.mat-card-actions-align-end{display:flex;justify-content:flex-end}.mat-card-image{width:calc(100% + 32px);margin:0 -16px 16px -16px;display:block;overflow:hidden}.mat-card-image img{width:100%}.mat-card-footer{display:block;margin:0 -16px -16px -16px}.mat-card-actions .mat-button,.mat-card-actions .mat-raised-button,.mat-card-actions .mat-stroked-button{margin:0 8px}.mat-card-header{display:flex;flex-direction:row}.mat-card-header .mat-card-title{margin-bottom:12px}.mat-card-header-text{margin:0 16px}.mat-card-avatar{height:40px;width:40px;border-radius:50%;flex-shrink:0;object-fit:cover}.mat-card-title-group{display:flex;justify-content:space-between}.mat-card-sm-image{width:80px;height:80px}.mat-card-md-image{width:112px;height:112px}.mat-card-lg-image{width:152px;height:152px}.mat-card-xl-image{width:240px;height:240px;margin:-8px}.mat-card-title-group>.mat-card-xl-image{margin:-8px 0 8px}@media(max-width: 599px){.mat-card-title-group{margin:0}.mat-card-xl-image{margin-left:0;margin-right:0}}.mat-card>:first-child,.mat-card-content>:first-child{margin-top:0}.mat-card>:last-child:not(.mat-card-footer),.mat-card-content>:last-child:not(.mat-card-footer){margin-bottom:0}.mat-card-image:first-child{margin-top:-16px;border-top-left-radius:inherit;border-top-right-radius:inherit}.mat-card>.mat-card-actions:last-child{margin-bottom:-8px;padding-bottom:0}.mat-card-actions:not(.mat-card-actions-align-end) .mat-button:first-child,.mat-card-actions:not(.mat-card-actions-align-end) .mat-raised-button:first-child,.mat-card-actions:not(.mat-card-actions-align-end) .mat-stroked-button:first-child{margin-left:0;margin-right:0}.mat-card-actions-align-end .mat-button:last-child,.mat-card-actions-align-end .mat-raised-button:last-child,.mat-card-actions-align-end .mat-stroked-button:last-child{margin-left:0;margin-right:0}.mat-card-title:not(:first-child),.mat-card-subtitle:not(:first-child){margin-top:-4px}.mat-card-header .mat-card-subtitle:not(:first-child){margin-top:-8px}.mat-card>.mat-card-xl-image:first-child{margin-top:-8px}.mat-card>.mat-card-xl-image:last-child{margin-bottom:-8px}\n"],
                encapsulation: 2,
                changeDetection: 0
            }),
            n
        }
        )()
          , $R = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["mat-card-header"]],
                hostAttrs: [1, "mat-card-header"],
                ngContentSelectors: VR,
                decls: 4,
                vars: 0,
                consts: [[1, "mat-card-header-text"]],
                template: function(t, r) {
                    1 & t && (hr(LR),
                    Be(0),
                    B(1, "div", 0),
                    Be(2, 1),
                    j(),
                    Be(3, 2))
                },
                encapsulation: 2,
                changeDetection: 0
            }),
            n
        }
        )()
          , GR = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[Et], Et]
            }),
            n
        }
        )();
        class zR extends It {
            constructor(e, t) {
                super()
            }
            schedule(e, t=0) {
                return this
            }
        }
        const rl = {
            setInterval(n, e, ...t) {
                const {delegate: r} = rl;
                return (null == r ? void 0 : r.setInterval) ? r.setInterval(n, e, ...t) : setInterval(n, e, ...t)
            },
            clearInterval(n) {
                const {delegate: e} = rl;
                return ((null == e ? void 0 : e.clearInterval) || clearInterval)(n)
            },
            delegate: void 0
        }
          , LD = {
            now: ()=>(LD.delegate || Date).now(),
            delegate: void 0
        };
        class Vo {
            constructor(e, t=Vo.now) {
                this.schedulerActionCtor = e,
                this.now = t
            }
            schedule(e, t=0, r) {
                return new this.schedulerActionCtor(this,e).schedule(r, t)
            }
        }
        Vo.now = LD.now;
        const KR = new class WR extends Vo {
            constructor(e, t=Vo.now) {
                super(e, t),
                this.actions = [],
                this._active = !1,
                this._scheduled = void 0
            }
            flush(e) {
                const {actions: t} = this;
                if (this._active)
                    return void t.push(e);
                let r;
                this._active = !0;
                do {
                    if (r = e.execute(e.state, e.delay))
                        break
                } while (e = t.shift());
                if (this._active = !1,
                r) {
                    for (; e = t.shift(); )
                        e.unsubscribe();
                    throw r
                }
            }
        }
        (class qR extends zR {
            constructor(e, t) {
                super(e, t),
                this.scheduler = e,
                this.work = t,
                this.pending = !1
            }
            schedule(e, t=0) {
                if (this.closed)
                    return this;
                this.state = e;
                const r = this.id
                  , i = this.scheduler;
                return null != r && (this.id = this.recycleAsyncId(i, r, t)),
                this.pending = !0,
                this.delay = t,
                this.id = this.id || this.requestAsyncId(i, this.id, t),
                this
            }
            requestAsyncId(e, t, r=0) {
                return rl.setInterval(e.flush.bind(e, this), r)
            }
            recycleAsyncId(e, t, r=0) {
                if (null != r && this.delay === r && !1 === this.pending)
                    return t;
                rl.clearInterval(t)
            }
            execute(e, t) {
                if (this.closed)
                    return new Error("executing a cancelled action");
                this.pending = !1;
                const r = this._execute(e, t);
                if (r)
                    return r;
                !1 === this.pending && null != this.id && (this.id = this.recycleAsyncId(this.scheduler, this.id, null))
            }
            _execute(e, t) {
                let i, r = !1;
                try {
                    this.work(e)
                } catch (o) {
                    r = !0,
                    i = o || new Error("Scheduled action threw falsy error")
                }
                if (r)
                    return this.unsubscribe(),
                    i
            }
            unsubscribe() {
                if (!this.closed) {
                    const {id: e, scheduler: t} = this
                      , {actions: r} = t;
                    this.work = this.state = this.scheduler = null,
                    this.pending = !1,
                    Fr(r, this),
                    null != e && (this.id = this.recycleAsyncId(t, e, null)),
                    this.delay = null,
                    super.unsubscribe()
                }
            }
        }
        );
        let VD = (()=>{
            class n {
                create(t) {
                    return "undefined" == typeof MutationObserver ? null : new MutationObserver(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )()
          , ZR = (()=>{
            class n {
                constructor(t) {
                    this._mutationObserverFactory = t,
                    this._observedElements = new Map
                }
                ngOnDestroy() {
                    this._observedElements.forEach((t,r)=>this._cleanupObserver(r))
                }
                observe(t) {
                    const r = Xn(t);
                    return new Fe(i=>{
                        const s = this._observeElement(r).subscribe(i);
                        return ()=>{
                            s.unsubscribe(),
                            this._unobserveElement(r)
                        }
                    }
                    )
                }
                _observeElement(t) {
                    if (this._observedElements.has(t))
                        this._observedElements.get(t).count++;
                    else {
                        const r = new Ut
                          , i = this._mutationObserverFactory.create(o=>r.next(o));
                        i && i.observe(t, {
                            characterData: !0,
                            childList: !0,
                            subtree: !0
                        }),
                        this._observedElements.set(t, {
                            observer: i,
                            stream: r,
                            count: 1
                        })
                    }
                    return this._observedElements.get(t).stream
                }
                _unobserveElement(t) {
                    this._observedElements.has(t) && (this._observedElements.get(t).count--,
                    this._observedElements.get(t).count || this._cleanupObserver(t))
                }
                _cleanupObserver(t) {
                    if (this._observedElements.has(t)) {
                        const {observer: r, stream: i} = this._observedElements.get(t);
                        r && r.disconnect(),
                        i.complete(),
                        this._observedElements.delete(t)
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(VD))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )()
          , YR = (()=>{
            class n {
                constructor(t, r, i) {
                    this._contentObserver = t,
                    this._elementRef = r,
                    this._ngZone = i,
                    this.event = new je,
                    this._disabled = !1,
                    this._currentSubscription = null
                }
                get disabled() {
                    return this._disabled
                }
                set disabled(t) {
                    this._disabled = Yn(t),
                    this._disabled ? this._unsubscribe() : this._subscribe()
                }
                get debounce() {
                    return this._debounce
                }
                set debounce(t) {
                    this._debounce = function eR(n, e=0) {
                        return function tR(n) {
                            return !isNaN(parseFloat(n)) && !isNaN(Number(n))
                        }(n) ? Number(n) : e
                    }(t),
                    this._subscribe()
                }
                ngAfterContentInit() {
                    !this._currentSubscription && !this.disabled && this._subscribe()
                }
                ngOnDestroy() {
                    this._unsubscribe()
                }
                _subscribe() {
                    this._unsubscribe();
                    const t = this._contentObserver.observe(this._elementRef);
                    this._ngZone.runOutsideAngular(()=>{
                        this._currentSubscription = (this.debounce ? t.pipe(function QR(n, e=KR) {
                            return st((t,r)=>{
                                let i = null
                                  , o = null
                                  , s = null;
                                const a = ()=>{
                                    if (i) {
                                        i.unsubscribe(),
                                        i = null;
                                        const u = o;
                                        o = null,
                                        r.next(u)
                                    }
                                }
                                ;
                                function l() {
                                    const u = s + n
                                      , c = e.now();
                                    if (c < u)
                                        return i = this.schedule(void 0, u - c),
                                        void r.add(i);
                                    a()
                                }
                                t.subscribe(St(r, u=>{
                                    o = u,
                                    s = e.now(),
                                    i || (i = e.schedule(l, n),
                                    r.add(i))
                                }
                                , ()=>{
                                    a(),
                                    r.complete()
                                }
                                , void 0, ()=>{
                                    o = i = null
                                }
                                ))
                            }
                            )
                        }(this.debounce)) : t).subscribe(this.event)
                    }
                    )
                }
                _unsubscribe() {
                    var t;
                    null === (t = this._currentSubscription) || void 0 === t || t.unsubscribe()
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(ZR),v(Pe),v(_e))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["", "cdkObserveContent", ""]],
                inputs: {
                    disabled: ["cdkObserveContentDisabled", "disabled"],
                    debounce: "debounce"
                },
                outputs: {
                    event: "cdkObserveContent"
                },
                exportAs: ["cdkObserveContent"]
            }),
            n
        }
        )()
          , XR = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                providers: [VD]
            }),
            n
        }
        )();
        const JR = ["addListener", "removeListener"]
          , eP = ["addEventListener", "removeEventListener"]
          , tP = ["on", "off"];
        function vf(n, e, t, r) {
            if (X(t) && (r = t,
            t = void 0),
            r)
                return vf(n, e, t).pipe(bv(r));
            const [i,o] = function iP(n) {
                return X(n.addEventListener) && X(n.removeEventListener)
            }(n) ? eP.map(s=>a=>n[s](e, a, t)) : function nP(n) {
                return X(n.addListener) && X(n.removeListener)
            }(n) ? JR.map(BD(n, e)) : function rP(n) {
                return X(n.on) && X(n.off)
            }(n) ? tP.map(BD(n, e)) : [];
            if (!i && pl(n))
                return xi(s=>vf(s, e, t))(rn(n));
            if (!i)
                throw new TypeError("Invalid event target");
            return new Fe(s=>{
                const a = (...l)=>s.next(1 < l.length ? l : l[0]);
                return i(a),
                ()=>o(a)
            }
            )
        }
        function BD(n, e) {
            return t=>r=>n[t](e, r)
        }
        function jD(...n) {
            return function oP() {
                return zf(1)
            }()(Fi(n, Ko(n)))
        }
        function bf(...n) {
            const e = Ko(n);
            return st((t,r)=>{
                (e ? jD(n, t, e) : jD(n, t)).subscribe(r)
            }
            )
        }
        const sP = ["connectionContainer"]
          , aP = ["inputContainer"]
          , lP = ["label"];
        function uP(n, e) {
            1 & n && (so(0),
            B(1, "div", 14),
            ke(2, "div", 15)(3, "div", 16)(4, "div", 17),
            j(),
            B(5, "div", 18),
            ke(6, "div", 15)(7, "div", 16)(8, "div", 17),
            j(),
            ao())
        }
        function cP(n, e) {
            if (1 & n) {
                const t = ac();
                B(0, "div", 19),
                Ke("cdkObserveContent", function() {
                    return Vl(t),
                    pn().updateOutlineGap()
                }),
                Be(1, 1),
                j()
            }
            2 & n && fe("cdkObserveContentDisabled", "outline" != pn().appearance)
        }
        function dP(n, e) {
            if (1 & n && (so(0),
            Be(1, 2),
            B(2, "span"),
            me(3),
            j(),
            ao()),
            2 & n) {
                const t = pn(2);
                de(3),
                pr(t._control.placeholder)
            }
        }
        function fP(n, e) {
            1 & n && Be(0, 3, ["*ngSwitchCase", "true"])
        }
        function hP(n, e) {
            1 & n && (B(0, "span", 23),
            me(1, " *"),
            j())
        }
        function pP(n, e) {
            if (1 & n) {
                const t = ac();
                B(0, "label", 20, 21),
                Ke("cdkObserveContent", function() {
                    return Vl(t),
                    pn().updateOutlineGap()
                }),
                ut(2, dP, 4, 1, "ng-container", 12),
                ut(3, fP, 1, 0, "ng-content", 12),
                ut(4, hP, 2, 0, "span", 22),
                j()
            }
            if (2 & n) {
                const t = pn();
                Je("mat-empty", t._control.empty && !t._shouldAlwaysFloat())("mat-form-field-empty", t._control.empty && !t._shouldAlwaysFloat())("mat-accent", "accent" == t.color)("mat-warn", "warn" == t.color),
                fe("cdkObserveContentDisabled", "outline" != t.appearance)("id", t._labelId)("ngSwitch", t._hasLabel()),
                bt("for", t._control.id)("aria-owns", t._control.id),
                de(2),
                fe("ngSwitchCase", !1),
                de(1),
                fe("ngSwitchCase", !0),
                de(1),
                fe("ngIf", !t.hideRequiredMarker && t._control.required && !t._control.disabled)
            }
        }
        function mP(n, e) {
            1 & n && (B(0, "div", 24),
            Be(1, 4),
            j())
        }
        function gP(n, e) {
            if (1 & n && (B(0, "div", 25),
            ke(1, "span", 26),
            j()),
            2 & n) {
                const t = pn();
                de(1),
                Je("mat-accent", "accent" == t.color)("mat-warn", "warn" == t.color)
            }
        }
        function yP(n, e) {
            1 & n && (B(0, "div"),
            Be(1, 5),
            j()),
            2 & n && fe("@transitionMessages", pn()._subscriptAnimationState)
        }
        function _P(n, e) {
            if (1 & n && (B(0, "div", 30),
            me(1),
            j()),
            2 & n) {
                const t = pn(2);
                fe("id", t._hintLabelId),
                de(1),
                pr(t.hintLabel)
            }
        }
        function vP(n, e) {
            if (1 & n && (B(0, "div", 27),
            ut(1, _P, 2, 2, "div", 28),
            Be(2, 6),
            ke(3, "div", 29),
            Be(4, 7),
            j()),
            2 & n) {
                const t = pn();
                fe("@transitionMessages", t._subscriptAnimationState),
                de(1),
                fe("ngIf", t.hintLabel)
            }
        }
        const bP = ["*", [["", "matPrefix", ""]], [["mat-placeholder"]], [["mat-label"]], [["", "matSuffix", ""]], [["mat-error"]], [["mat-hint", 3, "align", "end"]], [["mat-hint", "align", "end"]]]
          , DP = ["*", "[matPrefix]", "mat-placeholder", "mat-label", "[matSuffix]", "mat-error", "mat-hint:not([align='end'])", "mat-hint[align='end']"]
          , CP = new S("MatError")
          , EP = {
            transitionMessages: R1("transitionMessages", [L1("enter", Na({
                opacity: 1,
                transform: "translateY(0%)"
            })), V1("void => enter", [Na({
                opacity: 0,
                transform: "translateY(-5px)"
            }), P1("300ms cubic-bezier(0.55, 0, 0.55, 0.2)")])])
        };
        let Df = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n
            }),
            n
        }
        )();
        const wP = new S("MatHint");
        let Cf = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["mat-label"]]
            }),
            n
        }
        )()
          , MP = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["mat-placeholder"]]
            }),
            n
        }
        )();
        const AP = new S("MatPrefix")
          , TP = new S("MatSuffix");
        let HD = 0;
        const SP = nl(class {
            constructor(n) {
                this._elementRef = n
            }
        }
        , "primary")
          , xP = new S("MAT_FORM_FIELD_DEFAULT_OPTIONS")
          , $D = new S("MatFormField");
        let FP = (()=>{
            class n extends SP {
                constructor(t, r, i, o, s, a, l) {
                    super(t),
                    this._changeDetectorRef = r,
                    this._dir = i,
                    this._defaults = o,
                    this._platform = s,
                    this._ngZone = a,
                    this._outlineGapCalculationNeededImmediately = !1,
                    this._outlineGapCalculationNeededOnStable = !1,
                    this._destroyed = new Ut,
                    this._showAlwaysAnimate = !1,
                    this._subscriptAnimationState = "",
                    this._hintLabel = "",
                    this._hintLabelId = "mat-hint-" + HD++,
                    this._labelId = "mat-form-field-label-" + HD++,
                    this.floatLabel = this._getDefaultFloatLabelState(),
                    this._animationsEnabled = "NoopAnimations" !== l,
                    this.appearance = o && o.appearance ? o.appearance : "legacy",
                    this._hideRequiredMarker = !(!o || null == o.hideRequiredMarker) && o.hideRequiredMarker
                }
                get appearance() {
                    return this._appearance
                }
                set appearance(t) {
                    const r = this._appearance;
                    this._appearance = t || this._defaults && this._defaults.appearance || "legacy",
                    "outline" === this._appearance && r !== t && (this._outlineGapCalculationNeededOnStable = !0)
                }
                get hideRequiredMarker() {
                    return this._hideRequiredMarker
                }
                set hideRequiredMarker(t) {
                    this._hideRequiredMarker = Yn(t)
                }
                _shouldAlwaysFloat() {
                    return "always" === this.floatLabel && !this._showAlwaysAnimate
                }
                _canLabelFloat() {
                    return "never" !== this.floatLabel
                }
                get hintLabel() {
                    return this._hintLabel
                }
                set hintLabel(t) {
                    this._hintLabel = t,
                    this._processHints()
                }
                get floatLabel() {
                    return "legacy" !== this.appearance && "never" === this._floatLabel ? "auto" : this._floatLabel
                }
                set floatLabel(t) {
                    t !== this._floatLabel && (this._floatLabel = t || this._getDefaultFloatLabelState(),
                    this._changeDetectorRef.markForCheck())
                }
                get _control() {
                    return this._explicitFormFieldControl || this._controlNonStatic || this._controlStatic
                }
                set _control(t) {
                    this._explicitFormFieldControl = t
                }
                getLabelId() {
                    return this._hasFloatingLabel() ? this._labelId : null
                }
                getConnectedOverlayOrigin() {
                    return this._connectionContainerRef || this._elementRef
                }
                ngAfterContentInit() {
                    this._validateControlChild();
                    const t = this._control;
                    t.controlType && this._elementRef.nativeElement.classList.add(`mat-form-field-type-${t.controlType}`),
                    t.stateChanges.pipe(bf(null)).subscribe(()=>{
                        this._validatePlaceholders(),
                        this._syncDescribedByIds(),
                        this._changeDetectorRef.markForCheck()
                    }
                    ),
                    t.ngControl && t.ngControl.valueChanges && t.ngControl.valueChanges.pipe(el(this._destroyed)).subscribe(()=>this._changeDetectorRef.markForCheck()),
                    this._ngZone.runOutsideAngular(()=>{
                        this._ngZone.onStable.pipe(el(this._destroyed)).subscribe(()=>{
                            this._outlineGapCalculationNeededOnStable && this.updateOutlineGap()
                        }
                        )
                    }
                    ),
                    Qf(this._prefixChildren.changes, this._suffixChildren.changes).subscribe(()=>{
                        this._outlineGapCalculationNeededOnStable = !0,
                        this._changeDetectorRef.markForCheck()
                    }
                    ),
                    this._hintChildren.changes.pipe(bf(null)).subscribe(()=>{
                        this._processHints(),
                        this._changeDetectorRef.markForCheck()
                    }
                    ),
                    this._errorChildren.changes.pipe(bf(null)).subscribe(()=>{
                        this._syncDescribedByIds(),
                        this._changeDetectorRef.markForCheck()
                    }
                    ),
                    this._dir && this._dir.change.pipe(el(this._destroyed)).subscribe(()=>{
                        "function" == typeof requestAnimationFrame ? this._ngZone.runOutsideAngular(()=>{
                            requestAnimationFrame(()=>this.updateOutlineGap())
                        }
                        ) : this.updateOutlineGap()
                    }
                    )
                }
                ngAfterContentChecked() {
                    this._validateControlChild(),
                    this._outlineGapCalculationNeededImmediately && this.updateOutlineGap()
                }
                ngAfterViewInit() {
                    this._subscriptAnimationState = "enter",
                    this._changeDetectorRef.detectChanges()
                }
                ngOnDestroy() {
                    this._destroyed.next(),
                    this._destroyed.complete()
                }
                _shouldForward(t) {
                    const r = this._control ? this._control.ngControl : null;
                    return r && r[t]
                }
                _hasPlaceholder() {
                    return !!(this._control && this._control.placeholder || this._placeholderChild)
                }
                _hasLabel() {
                    return !(!this._labelChildNonStatic && !this._labelChildStatic)
                }
                _shouldLabelFloat() {
                    return this._canLabelFloat() && (this._control && this._control.shouldLabelFloat || this._shouldAlwaysFloat())
                }
                _hideControlPlaceholder() {
                    return "legacy" === this.appearance && !this._hasLabel() || this._hasLabel() && !this._shouldLabelFloat()
                }
                _hasFloatingLabel() {
                    return this._hasLabel() || "legacy" === this.appearance && this._hasPlaceholder()
                }
                _getDisplayedMessages() {
                    return this._errorChildren && this._errorChildren.length > 0 && this._control.errorState ? "error" : "hint"
                }
                _animateAndLockLabel() {
                    this._hasFloatingLabel() && this._canLabelFloat() && (this._animationsEnabled && this._label && (this._showAlwaysAnimate = !0,
                    vf(this._label.nativeElement, "transitionend").pipe(gl(1)).subscribe(()=>{
                        this._showAlwaysAnimate = !1
                    }
                    )),
                    this.floatLabel = "always",
                    this._changeDetectorRef.markForCheck())
                }
                _validatePlaceholders() {}
                _processHints() {
                    this._validateHints(),
                    this._syncDescribedByIds()
                }
                _validateHints() {}
                _getDefaultFloatLabelState() {
                    return this._defaults && this._defaults.floatLabel || "auto"
                }
                _syncDescribedByIds() {
                    if (this._control) {
                        let t = [];
                        if (this._control.userAriaDescribedBy && "string" == typeof this._control.userAriaDescribedBy && t.push(...this._control.userAriaDescribedBy.split(" ")),
                        "hint" === this._getDisplayedMessages()) {
                            const r = this._hintChildren ? this._hintChildren.find(o=>"start" === o.align) : null
                              , i = this._hintChildren ? this._hintChildren.find(o=>"end" === o.align) : null;
                            r ? t.push(r.id) : this._hintLabel && t.push(this._hintLabelId),
                            i && t.push(i.id)
                        } else
                            this._errorChildren && t.push(...this._errorChildren.map(r=>r.id));
                        this._control.setDescribedByIds(t)
                    }
                }
                _validateControlChild() {}
                updateOutlineGap() {
                    const t = this._label ? this._label.nativeElement : null
                      , r = this._connectionContainerRef.nativeElement
                      , i = ".mat-form-field-outline-start"
                      , o = ".mat-form-field-outline-gap";
                    if ("outline" !== this.appearance || !this._platform.isBrowser)
                        return;
                    if (!t || !t.children.length || !t.textContent.trim()) {
                        const c = r.querySelectorAll(`${i}, ${o}`);
                        for (let d = 0; d < c.length; d++)
                            c[d].style.width = "0";
                        return
                    }
                    if (!this._isAttachedToDOM())
                        return void (this._outlineGapCalculationNeededImmediately = !0);
                    let s = 0
                      , a = 0;
                    const l = r.querySelectorAll(i)
                      , u = r.querySelectorAll(o);
                    if (this._label && this._label.nativeElement.children.length) {
                        const c = r.getBoundingClientRect();
                        if (0 === c.width && 0 === c.height)
                            return this._outlineGapCalculationNeededOnStable = !0,
                            void (this._outlineGapCalculationNeededImmediately = !1);
                        const d = this._getStartEnd(c)
                          , f = t.children
                          , h = this._getStartEnd(f[0].getBoundingClientRect());
                        let p = 0;
                        for (let m = 0; m < f.length; m++)
                            p += f[m].offsetWidth;
                        s = Math.abs(h - d) - 5,
                        a = p > 0 ? .75 * p + 10 : 0
                    }
                    for (let c = 0; c < l.length; c++)
                        l[c].style.width = `${s}px`;
                    for (let c = 0; c < u.length; c++)
                        u[c].style.width = `${a}px`;
                    this._outlineGapCalculationNeededOnStable = this._outlineGapCalculationNeededImmediately = !1
                }
                _getStartEnd(t) {
                    return this._dir && "rtl" === this._dir.value ? t.right : t.left
                }
                _isAttachedToDOM() {
                    const t = this._elementRef.nativeElement;
                    if (t.getRootNode) {
                        const r = t.getRootNode();
                        return r && r !== t
                    }
                    return document.documentElement.contains(t)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Pe),v(Gc),v(jk, 8),v(xP, 8),v(Zn),v(_e),v(wi, 8))
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["mat-form-field"]],
                contentQueries: function(t, r, i) {
                    if (1 & t && (Jt(i, Df, 5),
                    Jt(i, Df, 7),
                    Jt(i, Cf, 5),
                    Jt(i, Cf, 7),
                    Jt(i, MP, 5),
                    Jt(i, CP, 5),
                    Jt(i, wP, 5),
                    Jt(i, AP, 5),
                    Jt(i, TP, 5)),
                    2 & t) {
                        let o;
                        tt(o = nt()) && (r._controlNonStatic = o.first),
                        tt(o = nt()) && (r._controlStatic = o.first),
                        tt(o = nt()) && (r._labelChildNonStatic = o.first),
                        tt(o = nt()) && (r._labelChildStatic = o.first),
                        tt(o = nt()) && (r._placeholderChild = o.first),
                        tt(o = nt()) && (r._errorChildren = o),
                        tt(o = nt()) && (r._hintChildren = o),
                        tt(o = nt()) && (r._prefixChildren = o),
                        tt(o = nt()) && (r._suffixChildren = o)
                    }
                },
                viewQuery: function(t, r) {
                    if (1 & t && (_o(sP, 7),
                    _o(aP, 5),
                    _o(lP, 5)),
                    2 & t) {
                        let i;
                        tt(i = nt()) && (r._connectionContainerRef = i.first),
                        tt(i = nt()) && (r._inputContainerRef = i.first),
                        tt(i = nt()) && (r._label = i.first)
                    }
                },
                hostAttrs: [1, "mat-form-field"],
                hostVars: 40,
                hostBindings: function(t, r) {
                    2 & t && Je("mat-form-field-appearance-standard", "standard" == r.appearance)("mat-form-field-appearance-fill", "fill" == r.appearance)("mat-form-field-appearance-outline", "outline" == r.appearance)("mat-form-field-appearance-legacy", "legacy" == r.appearance)("mat-form-field-invalid", r._control.errorState)("mat-form-field-can-float", r._canLabelFloat())("mat-form-field-should-float", r._shouldLabelFloat())("mat-form-field-has-label", r._hasFloatingLabel())("mat-form-field-hide-placeholder", r._hideControlPlaceholder())("mat-form-field-disabled", r._control.disabled)("mat-form-field-autofilled", r._control.autofilled)("mat-focused", r._control.focused)("ng-untouched", r._shouldForward("untouched"))("ng-touched", r._shouldForward("touched"))("ng-pristine", r._shouldForward("pristine"))("ng-dirty", r._shouldForward("dirty"))("ng-valid", r._shouldForward("valid"))("ng-invalid", r._shouldForward("invalid"))("ng-pending", r._shouldForward("pending"))("_mat-animation-noopable", !r._animationsEnabled)
                },
                inputs: {
                    color: "color",
                    appearance: "appearance",
                    hideRequiredMarker: "hideRequiredMarker",
                    hintLabel: "hintLabel",
                    floatLabel: "floatLabel"
                },
                exportAs: ["matFormField"],
                features: [ae([{
                    provide: $D,
                    useExisting: n
                }]), Y],
                ngContentSelectors: DP,
                decls: 15,
                vars: 8,
                consts: [[1, "mat-form-field-wrapper"], [1, "mat-form-field-flex", 3, "click"], ["connectionContainer", ""], [4, "ngIf"], ["class", "mat-form-field-prefix", 3, "cdkObserveContentDisabled", "cdkObserveContent", 4, "ngIf"], [1, "mat-form-field-infix"], ["inputContainer", ""], [1, "mat-form-field-label-wrapper"], ["class", "mat-form-field-label", 3, "cdkObserveContentDisabled", "id", "mat-empty", "mat-form-field-empty", "mat-accent", "mat-warn", "ngSwitch", "cdkObserveContent", 4, "ngIf"], ["class", "mat-form-field-suffix", 4, "ngIf"], ["class", "mat-form-field-underline", 4, "ngIf"], [1, "mat-form-field-subscript-wrapper", 3, "ngSwitch"], [4, "ngSwitchCase"], ["class", "mat-form-field-hint-wrapper", 4, "ngSwitchCase"], [1, "mat-form-field-outline"], [1, "mat-form-field-outline-start"], [1, "mat-form-field-outline-gap"], [1, "mat-form-field-outline-end"], [1, "mat-form-field-outline", "mat-form-field-outline-thick"], [1, "mat-form-field-prefix", 3, "cdkObserveContentDisabled", "cdkObserveContent"], [1, "mat-form-field-label", 3, "cdkObserveContentDisabled", "id", "ngSwitch", "cdkObserveContent"], ["label", ""], ["class", "mat-placeholder-required mat-form-field-required-marker", "aria-hidden", "true", 4, "ngIf"], ["aria-hidden", "true", 1, "mat-placeholder-required", "mat-form-field-required-marker"], [1, "mat-form-field-suffix"], [1, "mat-form-field-underline"], [1, "mat-form-field-ripple"], [1, "mat-form-field-hint-wrapper"], ["class", "mat-hint", 3, "id", 4, "ngIf"], [1, "mat-form-field-hint-spacer"], [1, "mat-hint", 3, "id"]],
                template: function(t, r) {
                    1 & t && (hr(bP),
                    B(0, "div", 0)(1, "div", 1, 2),
                    Ke("click", function(o) {
                        return r._control.onContainerClick && r._control.onContainerClick(o)
                    }),
                    ut(3, uP, 9, 0, "ng-container", 3),
                    ut(4, cP, 2, 1, "div", 4),
                    B(5, "div", 5, 6),
                    Be(7),
                    B(8, "span", 7),
                    ut(9, pP, 5, 16, "label", 8),
                    j()(),
                    ut(10, mP, 2, 0, "div", 9),
                    j(),
                    ut(11, gP, 2, 4, "div", 10),
                    B(12, "div", 11),
                    ut(13, yP, 2, 1, "div", 12),
                    ut(14, vP, 5, 2, "div", 13),
                    j()()),
                    2 & t && (de(3),
                    fe("ngIf", "outline" == r.appearance),
                    de(1),
                    fe("ngIf", r._prefixChildren.length),
                    de(5),
                    fe("ngIf", r._hasFloatingLabel()),
                    de(1),
                    fe("ngIf", r._suffixChildren.length),
                    de(1),
                    fe("ngIf", "outline" != r.appearance),
                    de(1),
                    fe("ngSwitch", r._getDisplayedMessages()),
                    de(1),
                    fe("ngSwitchCase", "error"),
                    de(1),
                    fe("ngSwitchCase", "hint"))
                },
                directives: [V_, YR, fa, j_],
                styles: [".mat-form-field{display:inline-block;position:relative;text-align:left}[dir=rtl] .mat-form-field{text-align:right}.mat-form-field-wrapper{position:relative}.mat-form-field-flex{display:inline-flex;align-items:baseline;box-sizing:border-box;width:100%}.mat-form-field-prefix,.mat-form-field-suffix{white-space:nowrap;flex:none;position:relative}.mat-form-field-infix{display:block;position:relative;flex:auto;min-width:0;width:180px}.cdk-high-contrast-active .mat-form-field-infix{border-image:linear-gradient(transparent, transparent)}.mat-form-field-label-wrapper{position:absolute;left:0;box-sizing:content-box;width:100%;height:100%;overflow:hidden;pointer-events:none}[dir=rtl] .mat-form-field-label-wrapper{left:auto;right:0}.mat-form-field-label{position:absolute;left:0;font:inherit;pointer-events:none;width:100%;white-space:nowrap;text-overflow:ellipsis;overflow:hidden;transform-origin:0 0;transition:transform 400ms cubic-bezier(0.25, 0.8, 0.25, 1),color 400ms cubic-bezier(0.25, 0.8, 0.25, 1),width 400ms cubic-bezier(0.25, 0.8, 0.25, 1);display:none}[dir=rtl] .mat-form-field-label{transform-origin:100% 0;left:auto;right:0}.cdk-high-contrast-active .mat-form-field-disabled .mat-form-field-label{color:GrayText}.mat-form-field-empty.mat-form-field-label,.mat-form-field-can-float.mat-form-field-should-float .mat-form-field-label{display:block}.mat-form-field-autofill-control:-webkit-autofill+.mat-form-field-label-wrapper .mat-form-field-label{display:none}.mat-form-field-can-float .mat-form-field-autofill-control:-webkit-autofill+.mat-form-field-label-wrapper .mat-form-field-label{display:block;transition:none}.mat-input-server:focus+.mat-form-field-label-wrapper .mat-form-field-label,.mat-input-server[placeholder]:not(:placeholder-shown)+.mat-form-field-label-wrapper .mat-form-field-label{display:none}.mat-form-field-can-float .mat-input-server:focus+.mat-form-field-label-wrapper .mat-form-field-label,.mat-form-field-can-float .mat-input-server[placeholder]:not(:placeholder-shown)+.mat-form-field-label-wrapper .mat-form-field-label{display:block}.mat-form-field-label:not(.mat-form-field-empty){transition:none}.mat-form-field-underline{position:absolute;width:100%;pointer-events:none;transform:scale3d(1, 1.0001, 1)}.mat-form-field-ripple{position:absolute;left:0;width:100%;transform-origin:50%;transform:scaleX(0.5);opacity:0;transition:background-color 300ms cubic-bezier(0.55, 0, 0.55, 0.2)}.mat-form-field.mat-focused .mat-form-field-ripple,.mat-form-field.mat-form-field-invalid .mat-form-field-ripple{opacity:1;transform:none;transition:transform 300ms cubic-bezier(0.25, 0.8, 0.25, 1),opacity 100ms cubic-bezier(0.25, 0.8, 0.25, 1),background-color 300ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-form-field-subscript-wrapper{position:absolute;box-sizing:border-box;width:100%;overflow:hidden}.mat-form-field-subscript-wrapper .mat-icon,.mat-form-field-label-wrapper .mat-icon{width:1em;height:1em;font-size:inherit;vertical-align:baseline}.mat-form-field-hint-wrapper{display:flex}.mat-form-field-hint-spacer{flex:1 0 1em}.mat-error{display:block}.mat-form-field-control-wrapper{position:relative}.mat-form-field-hint-end{order:1}.mat-form-field._mat-animation-noopable .mat-form-field-label,.mat-form-field._mat-animation-noopable .mat-form-field-ripple{transition:none}\n", '.mat-form-field-appearance-fill .mat-form-field-flex{border-radius:4px 4px 0 0;padding:.75em .75em 0 .75em}.cdk-high-contrast-active .mat-form-field-appearance-fill .mat-form-field-flex{outline:solid 1px}.cdk-high-contrast-active .mat-form-field-appearance-fill.mat-form-field-disabled .mat-form-field-flex{outline-color:GrayText}.cdk-high-contrast-active .mat-form-field-appearance-fill.mat-focused .mat-form-field-flex{outline:dashed 3px}.mat-form-field-appearance-fill .mat-form-field-underline::before{content:"";display:block;position:absolute;bottom:0;height:1px;width:100%}.mat-form-field-appearance-fill .mat-form-field-ripple{bottom:0;height:2px}.cdk-high-contrast-active .mat-form-field-appearance-fill .mat-form-field-ripple{height:0}.mat-form-field-appearance-fill:not(.mat-form-field-disabled) .mat-form-field-flex:hover~.mat-form-field-underline .mat-form-field-ripple{opacity:1;transform:none;transition:opacity 600ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-form-field-appearance-fill._mat-animation-noopable:not(.mat-form-field-disabled) .mat-form-field-flex:hover~.mat-form-field-underline .mat-form-field-ripple{transition:none}.mat-form-field-appearance-fill .mat-form-field-subscript-wrapper{padding:0 1em}\n', '.mat-input-element{font:inherit;background:transparent;color:currentColor;border:none;outline:none;padding:0;margin:0;width:100%;max-width:100%;vertical-align:bottom;text-align:inherit;box-sizing:content-box}.mat-input-element:-moz-ui-invalid{box-shadow:none}.mat-input-element,.mat-input-element::-webkit-search-cancel-button,.mat-input-element::-webkit-search-decoration,.mat-input-element::-webkit-search-results-button,.mat-input-element::-webkit-search-results-decoration{-webkit-appearance:none}.mat-input-element::-webkit-contacts-auto-fill-button,.mat-input-element::-webkit-caps-lock-indicator,.mat-input-element:not([type=password])::-webkit-credentials-auto-fill-button{visibility:hidden}.mat-input-element[type=date],.mat-input-element[type=datetime],.mat-input-element[type=datetime-local],.mat-input-element[type=month],.mat-input-element[type=week],.mat-input-element[type=time]{line-height:1}.mat-input-element[type=date]::after,.mat-input-element[type=datetime]::after,.mat-input-element[type=datetime-local]::after,.mat-input-element[type=month]::after,.mat-input-element[type=week]::after,.mat-input-element[type=time]::after{content:" ";white-space:pre;width:1px}.mat-input-element::-webkit-inner-spin-button,.mat-input-element::-webkit-calendar-picker-indicator,.mat-input-element::-webkit-clear-button{font-size:.75em}.mat-input-element::placeholder{-webkit-user-select:none;user-select:none;transition:color 400ms 133.3333333333ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-input-element::-moz-placeholder{-webkit-user-select:none;user-select:none;transition:color 400ms 133.3333333333ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-input-element::-webkit-input-placeholder{-webkit-user-select:none;user-select:none;transition:color 400ms 133.3333333333ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-input-element:-ms-input-placeholder{-webkit-user-select:none;user-select:none;transition:color 400ms 133.3333333333ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-form-field-hide-placeholder .mat-input-element::placeholder{color:transparent !important;-webkit-text-fill-color:transparent;transition:none}.cdk-high-contrast-active .mat-form-field-hide-placeholder .mat-input-element::placeholder{opacity:0}.mat-form-field-hide-placeholder .mat-input-element::-moz-placeholder{color:transparent !important;-webkit-text-fill-color:transparent;transition:none}.cdk-high-contrast-active .mat-form-field-hide-placeholder .mat-input-element::-moz-placeholder{opacity:0}.mat-form-field-hide-placeholder .mat-input-element::-webkit-input-placeholder{color:transparent !important;-webkit-text-fill-color:transparent;transition:none}.cdk-high-contrast-active .mat-form-field-hide-placeholder .mat-input-element::-webkit-input-placeholder{opacity:0}.mat-form-field-hide-placeholder .mat-input-element:-ms-input-placeholder{color:transparent !important;-webkit-text-fill-color:transparent;transition:none}.cdk-high-contrast-active .mat-form-field-hide-placeholder .mat-input-element:-ms-input-placeholder{opacity:0}textarea.mat-input-element{resize:vertical;overflow:auto}textarea.mat-input-element.cdk-textarea-autosize{resize:none}textarea.mat-input-element{padding:2px 0;margin:-2px 0}select.mat-input-element{-moz-appearance:none;-webkit-appearance:none;position:relative;background-color:transparent;display:inline-flex;box-sizing:border-box;padding-top:1em;top:-1em;margin-bottom:-1em}select.mat-input-element::-moz-focus-inner{border:0}select.mat-input-element:not(:disabled){cursor:pointer}.mat-form-field-type-mat-native-select .mat-form-field-infix::after{content:"";width:0;height:0;border-left:5px solid transparent;border-right:5px solid transparent;border-top:5px solid;position:absolute;top:50%;right:0;margin-top:-2.5px;pointer-events:none}[dir=rtl] .mat-form-field-type-mat-native-select .mat-form-field-infix::after{right:auto;left:0}.mat-form-field-type-mat-native-select .mat-input-element{padding-right:15px}[dir=rtl] .mat-form-field-type-mat-native-select .mat-input-element{padding-right:0;padding-left:15px}.mat-form-field-type-mat-native-select .mat-form-field-label-wrapper{max-width:calc(100% - 10px)}.mat-form-field-type-mat-native-select.mat-form-field-appearance-outline .mat-form-field-infix::after{margin-top:-5px}.mat-form-field-type-mat-native-select.mat-form-field-appearance-fill .mat-form-field-infix::after{margin-top:-10px}\n', ".mat-form-field-appearance-legacy .mat-form-field-label{transform:perspective(100px)}.mat-form-field-appearance-legacy .mat-form-field-prefix .mat-icon,.mat-form-field-appearance-legacy .mat-form-field-suffix .mat-icon{width:1em}.mat-form-field-appearance-legacy .mat-form-field-prefix .mat-icon-button,.mat-form-field-appearance-legacy .mat-form-field-suffix .mat-icon-button{font:inherit;vertical-align:baseline}.mat-form-field-appearance-legacy .mat-form-field-prefix .mat-icon-button .mat-icon,.mat-form-field-appearance-legacy .mat-form-field-suffix .mat-icon-button .mat-icon{font-size:inherit}.mat-form-field-appearance-legacy .mat-form-field-underline{height:1px}.cdk-high-contrast-active .mat-form-field-appearance-legacy .mat-form-field-underline{height:0;border-top:solid 1px}.mat-form-field-appearance-legacy .mat-form-field-ripple{top:0;height:2px;overflow:hidden}.cdk-high-contrast-active .mat-form-field-appearance-legacy .mat-form-field-ripple{height:0;border-top:solid 2px}.mat-form-field-appearance-legacy.mat-form-field-disabled .mat-form-field-underline{background-position:0;background-color:transparent}.cdk-high-contrast-active .mat-form-field-appearance-legacy.mat-form-field-disabled .mat-form-field-underline{border-top-style:dotted;border-top-width:2px;border-top-color:GrayText}.mat-form-field-appearance-legacy.mat-form-field-invalid:not(.mat-focused) .mat-form-field-ripple{height:1px}\n", ".mat-form-field-appearance-outline .mat-form-field-wrapper{margin:.25em 0}.mat-form-field-appearance-outline .mat-form-field-flex{padding:0 .75em 0 .75em;margin-top:-0.25em;position:relative}.mat-form-field-appearance-outline .mat-form-field-prefix,.mat-form-field-appearance-outline .mat-form-field-suffix{top:.25em}.mat-form-field-appearance-outline .mat-form-field-outline{display:flex;position:absolute;top:.25em;left:0;right:0;bottom:0;pointer-events:none}.mat-form-field-appearance-outline .mat-form-field-outline-start,.mat-form-field-appearance-outline .mat-form-field-outline-end{border:1px solid currentColor;min-width:5px}.mat-form-field-appearance-outline .mat-form-field-outline-start{border-radius:5px 0 0 5px;border-right-style:none}[dir=rtl] .mat-form-field-appearance-outline .mat-form-field-outline-start{border-right-style:solid;border-left-style:none;border-radius:0 5px 5px 0}.mat-form-field-appearance-outline .mat-form-field-outline-end{border-radius:0 5px 5px 0;border-left-style:none;flex-grow:1}[dir=rtl] .mat-form-field-appearance-outline .mat-form-field-outline-end{border-left-style:solid;border-right-style:none;border-radius:5px 0 0 5px}.mat-form-field-appearance-outline .mat-form-field-outline-gap{border-radius:.000001px;border:1px solid currentColor;border-left-style:none;border-right-style:none}.mat-form-field-appearance-outline.mat-form-field-can-float.mat-form-field-should-float .mat-form-field-outline-gap{border-top-color:transparent}.mat-form-field-appearance-outline .mat-form-field-outline-thick{opacity:0}.mat-form-field-appearance-outline .mat-form-field-outline-thick .mat-form-field-outline-start,.mat-form-field-appearance-outline .mat-form-field-outline-thick .mat-form-field-outline-end,.mat-form-field-appearance-outline .mat-form-field-outline-thick .mat-form-field-outline-gap{border-width:2px}.mat-form-field-appearance-outline.mat-focused .mat-form-field-outline,.mat-form-field-appearance-outline.mat-form-field-invalid .mat-form-field-outline{opacity:0;transition:opacity 100ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-form-field-appearance-outline.mat-focused .mat-form-field-outline-thick,.mat-form-field-appearance-outline.mat-form-field-invalid .mat-form-field-outline-thick{opacity:1}.cdk-high-contrast-active .mat-form-field-appearance-outline.mat-focused .mat-form-field-outline-thick{border:3px dashed}.mat-form-field-appearance-outline:not(.mat-form-field-disabled) .mat-form-field-flex:hover .mat-form-field-outline{opacity:0;transition:opacity 600ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-form-field-appearance-outline:not(.mat-form-field-disabled) .mat-form-field-flex:hover .mat-form-field-outline-thick{opacity:1}.mat-form-field-appearance-outline .mat-form-field-subscript-wrapper{padding:0 1em}.cdk-high-contrast-active .mat-form-field-appearance-outline.mat-form-field-disabled .mat-form-field-outline{color:GrayText}.mat-form-field-appearance-outline._mat-animation-noopable:not(.mat-form-field-disabled) .mat-form-field-flex:hover~.mat-form-field-outline,.mat-form-field-appearance-outline._mat-animation-noopable .mat-form-field-outline,.mat-form-field-appearance-outline._mat-animation-noopable .mat-form-field-outline-start,.mat-form-field-appearance-outline._mat-animation-noopable .mat-form-field-outline-end,.mat-form-field-appearance-outline._mat-animation-noopable .mat-form-field-outline-gap{transition:none}\n", ".mat-form-field-appearance-standard .mat-form-field-flex{padding-top:.75em}.mat-form-field-appearance-standard .mat-form-field-underline{height:1px}.cdk-high-contrast-active .mat-form-field-appearance-standard .mat-form-field-underline{height:0;border-top:solid 1px}.mat-form-field-appearance-standard .mat-form-field-ripple{bottom:0;height:2px}.cdk-high-contrast-active .mat-form-field-appearance-standard .mat-form-field-ripple{height:0;border-top:solid 2px}.mat-form-field-appearance-standard.mat-form-field-disabled .mat-form-field-underline{background-position:0;background-color:transparent}.cdk-high-contrast-active .mat-form-field-appearance-standard.mat-form-field-disabled .mat-form-field-underline{border-top-style:dotted;border-top-width:2px}.mat-form-field-appearance-standard:not(.mat-form-field-disabled) .mat-form-field-flex:hover~.mat-form-field-underline .mat-form-field-ripple{opacity:1;transform:none;transition:opacity 600ms cubic-bezier(0.25, 0.8, 0.25, 1)}.mat-form-field-appearance-standard._mat-animation-noopable:not(.mat-form-field-disabled) .mat-form-field-flex:hover~.mat-form-field-underline .mat-form-field-ripple{transition:none}\n"],
                encapsulation: 2,
                data: {
                    animation: [EP.transitionMessages]
                },
                changeDetection: 0
            }),
            n
        }
        )()
          , Ef = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[$_, Et, XR], Et]
            }),
            n
        }
        )();
        function wf(n, e, t) {
            const r = X(n) || e || t ? {
                next: n,
                error: e,
                complete: t
            } : n;
            return r ? st((i,o)=>{
                var s;
                null === (s = r.subscribe) || void 0 === s || s.call(r);
                let a = !0;
                i.subscribe(St(o, l=>{
                    var u;
                    null === (u = r.next) || void 0 === u || u.call(r, l),
                    o.next(l)
                }
                , ()=>{
                    var l;
                    a = !1,
                    null === (l = r.complete) || void 0 === l || l.call(r),
                    o.complete()
                }
                , l=>{
                    var u;
                    a = !1,
                    null === (u = r.error) || void 0 === u || u.call(r, l),
                    o.error(l)
                }
                , ()=>{
                    var l, u;
                    a && (null === (l = r.unsubscribe) || void 0 === l || l.call(r)),
                    null === (u = r.finalize) || void 0 === u || u.call(r)
                }
                ))
            }
            ) : qo
        }
        function GD(n) {
            return st((e,t)=>{
                let o, r = null, i = !1;
                r = e.subscribe(St(t, void 0, void 0, s=>{
                    o = rn(n(s, GD(n)(e))),
                    r ? (r.unsubscribe(),
                    r = null,
                    o.subscribe(t)) : i = !0
                }
                )),
                i && (r.unsubscribe(),
                r = null,
                o.subscribe(t))
            }
            )
        }
        const kP = ["*"];
        let il;
        function Bo(n) {
            var e;
            return (null === (e = function RP() {
                if (void 0 === il && (il = null,
                "undefined" != typeof window)) {
                    const n = window;
                    void 0 !== n.trustedTypes && (il = n.trustedTypes.createPolicy("angular#components", {
                        createHTML: e=>e
                    }))
                }
                return il
            }()) || void 0 === e ? void 0 : e.createHTML(n)) || n
        }
        function zD(n) {
            return Error(`Unable to find icon with the name "${n}"`)
        }
        function qD(n) {
            return Error(`The URL provided to MatIconRegistry was not trusted as a resource URL via Angular's DomSanitizer. Attempted URL was "${n}".`)
        }
        function WD(n) {
            return Error(`The literal provided to MatIconRegistry was not trusted as safe HTML by Angular's DomSanitizer. Attempted literal was "${n}".`)
        }
        class Ir {
            constructor(e, t, r) {
                this.url = e,
                this.svgText = t,
                this.options = r
            }
        }
        let ol = (()=>{
            class n {
                constructor(t, r, i, o) {
                    this._httpClient = t,
                    this._sanitizer = r,
                    this._errorHandler = o,
                    this._svgIconConfigs = new Map,
                    this._iconSetConfigs = new Map,
                    this._cachedIconsByUrl = new Map,
                    this._inProgressUrlFetches = new Map,
                    this._fontCssClassesByAlias = new Map,
                    this._resolvers = [],
                    this._defaultFontSetClass = "material-icons",
                    this._document = i
                }
                addSvgIcon(t, r, i) {
                    return this.addSvgIconInNamespace("", t, r, i)
                }
                addSvgIconLiteral(t, r, i) {
                    return this.addSvgIconLiteralInNamespace("", t, r, i)
                }
                addSvgIconInNamespace(t, r, i, o) {
                    return this._addSvgIconConfig(t, r, new Ir(i,null,o))
                }
                addSvgIconResolver(t) {
                    return this._resolvers.push(t),
                    this
                }
                addSvgIconLiteralInNamespace(t, r, i, o) {
                    const s = this._sanitizer.sanitize(ee.HTML, i);
                    if (!s)
                        throw WD(i);
                    const a = Bo(s);
                    return this._addSvgIconConfig(t, r, new Ir("",a,o))
                }
                addSvgIconSet(t, r) {
                    return this.addSvgIconSetInNamespace("", t, r)
                }
                addSvgIconSetLiteral(t, r) {
                    return this.addSvgIconSetLiteralInNamespace("", t, r)
                }
                addSvgIconSetInNamespace(t, r, i) {
                    return this._addSvgIconSetConfig(t, new Ir(r,null,i))
                }
                addSvgIconSetLiteralInNamespace(t, r, i) {
                    const o = this._sanitizer.sanitize(ee.HTML, r);
                    if (!o)
                        throw WD(r);
                    const s = Bo(o);
                    return this._addSvgIconSetConfig(t, new Ir("",s,i))
                }
                registerFontClassAlias(t, r=t) {
                    return this._fontCssClassesByAlias.set(t, r),
                    this
                }
                classNameForFontAlias(t) {
                    return this._fontCssClassesByAlias.get(t) || t
                }
                setDefaultFontSetClass(t) {
                    return this._defaultFontSetClass = t,
                    this
                }
                getDefaultFontSetClass() {
                    return this._defaultFontSetClass
                }
                getSvgIconFromUrl(t) {
                    const r = this._sanitizer.sanitize(ee.RESOURCE_URL, t);
                    if (!r)
                        throw qD(t);
                    const i = this._cachedIconsByUrl.get(r);
                    return i ? br(sl(i)) : this._loadSvgIconFromConfig(new Ir(t,null)).pipe(wf(o=>this._cachedIconsByUrl.set(r, o)), xt(o=>sl(o)))
                }
                getNamedSvgIcon(t, r="") {
                    const i = KD(r, t);
                    let o = this._svgIconConfigs.get(i);
                    if (o)
                        return this._getSvgFromConfig(o);
                    if (o = this._getIconConfigFromResolvers(r, t),
                    o)
                        return this._svgIconConfigs.set(i, o),
                        this._getSvgFromConfig(o);
                    const s = this._iconSetConfigs.get(r);
                    return s ? this._getSvgFromIconSetConfigs(t, s) : function NP(n, e) {
                        const t = X(n) ? n : ()=>n
                          , r = i=>i.error(t());
                        return new Fe(e ? i=>e.schedule(r, 0, i) : r)
                    }(zD(i))
                }
                ngOnDestroy() {
                    this._resolvers = [],
                    this._svgIconConfigs.clear(),
                    this._iconSetConfigs.clear(),
                    this._cachedIconsByUrl.clear()
                }
                _getSvgFromConfig(t) {
                    return t.svgText ? br(sl(this._svgElementFromConfig(t))) : this._loadSvgIconFromConfig(t).pipe(xt(r=>sl(r)))
                }
                _getSvgFromIconSetConfigs(t, r) {
                    const i = this._extractIconWithNameFromAnySet(t, r);
                    return i ? br(i) : Dv(r.filter(s=>!s.svgText).map(s=>this._loadSvgIconSetFromConfig(s).pipe(GD(a=>{
                        const u = `Loading icon set URL: ${this._sanitizer.sanitize(ee.RESOURCE_URL, s.url)} failed: ${a.message}`;
                        return this._errorHandler.handleError(new Error(u)),
                        br(null)
                    }
                    )))).pipe(xt(()=>{
                        const s = this._extractIconWithNameFromAnySet(t, r);
                        if (!s)
                            throw zD(t);
                        return s
                    }
                    ))
                }
                _extractIconWithNameFromAnySet(t, r) {
                    for (let i = r.length - 1; i >= 0; i--) {
                        const o = r[i];
                        if (o.svgText && o.svgText.toString().indexOf(t) > -1) {
                            const s = this._svgElementFromConfig(o)
                              , a = this._extractSvgIconFromSet(s, t, o.options);
                            if (a)
                                return a
                        }
                    }
                    return null
                }
                _loadSvgIconFromConfig(t) {
                    return this._fetchIcon(t).pipe(wf(r=>t.svgText = r), xt(()=>this._svgElementFromConfig(t)))
                }
                _loadSvgIconSetFromConfig(t) {
                    return t.svgText ? br(null) : this._fetchIcon(t).pipe(wf(r=>t.svgText = r))
                }
                _extractSvgIconFromSet(t, r, i) {
                    const o = t.querySelector(`[id="${r}"]`);
                    if (!o)
                        return null;
                    const s = o.cloneNode(!0);
                    if (s.removeAttribute("id"),
                    "svg" === s.nodeName.toLowerCase())
                        return this._setSvgAttributes(s, i);
                    if ("symbol" === s.nodeName.toLowerCase())
                        return this._setSvgAttributes(this._toSvgElement(s), i);
                    const a = this._svgElementFromString(Bo("<svg></svg>"));
                    return a.appendChild(s),
                    this._setSvgAttributes(a, i)
                }
                _svgElementFromString(t) {
                    const r = this._document.createElement("DIV");
                    r.innerHTML = t;
                    const i = r.querySelector("svg");
                    if (!i)
                        throw Error("<svg> tag not found");
                    return i
                }
                _toSvgElement(t) {
                    const r = this._svgElementFromString(Bo("<svg></svg>"))
                      , i = t.attributes;
                    for (let o = 0; o < i.length; o++) {
                        const {name: s, value: a} = i[o];
                        "id" !== s && r.setAttribute(s, a)
                    }
                    for (let o = 0; o < t.childNodes.length; o++)
                        t.childNodes[o].nodeType === this._document.ELEMENT_NODE && r.appendChild(t.childNodes[o].cloneNode(!0));
                    return r
                }
                _setSvgAttributes(t, r) {
                    return t.setAttribute("fit", ""),
                    t.setAttribute("height", "100%"),
                    t.setAttribute("width", "100%"),
                    t.setAttribute("preserveAspectRatio", "xMidYMid meet"),
                    t.setAttribute("focusable", "false"),
                    r && r.viewBox && t.setAttribute("viewBox", r.viewBox),
                    t
                }
                _fetchIcon(t) {
                    var r;
                    const {url: i, options: o} = t
                      , s = null !== (r = null == o ? void 0 : o.withCredentials) && void 0 !== r && r;
                    if (!this._httpClient)
                        throw function PP() {
                            return Error("Could not find HttpClient provider for use with Angular Material icons. Please include the HttpClientModule from @angular/common/http in your app imports.")
                        }();
                    if (null == i)
                        throw Error(`Cannot fetch icon from URL "${i}".`);
                    const a = this._sanitizer.sanitize(ee.RESOURCE_URL, i);
                    if (!a)
                        throw qD(i);
                    const l = this._inProgressUrlFetches.get(a);
                    if (l)
                        return l;
                    const u = this._httpClient.get(a, {
                        responseType: "text",
                        withCredentials: s
                    }).pipe(xt(c=>Bo(c)), function OP(n) {
                        return st((e,t)=>{
                            try {
                                e.subscribe(t)
                            } finally {
                                t.add(n)
                            }
                        }
                        )
                    }(()=>this._inProgressUrlFetches.delete(a)), Zf());
                    return this._inProgressUrlFetches.set(a, u),
                    u
                }
                _addSvgIconConfig(t, r, i) {
                    return this._svgIconConfigs.set(KD(t, r), i),
                    this
                }
                _addSvgIconSetConfig(t, r) {
                    const i = this._iconSetConfigs.get(t);
                    return i ? i.push(r) : this._iconSetConfigs.set(t, [r]),
                    this
                }
                _svgElementFromConfig(t) {
                    if (!t.svgElement) {
                        const r = this._svgElementFromString(t.svgText);
                        this._setSvgAttributes(r, t.options),
                        t.svgElement = r
                    }
                    return t.svgElement
                }
                _getIconConfigFromResolvers(t, r) {
                    for (let i = 0; i < this._resolvers.length; i++) {
                        const o = this._resolvers[i](r, t);
                        if (o)
                            return VP(o) ? new Ir(o.url,null,o.options) : new Ir(o,null)
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(va, 8),w(hd),w(ge, 8),w(Hn))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )();
        function sl(n) {
            return n.cloneNode(!0)
        }
        function KD(n, e) {
            return n + ":" + e
        }
        function VP(n) {
            return !(!n.url || !n.options)
        }
        const BP = nl(class {
            constructor(n) {
                this._elementRef = n
            }
        }
        )
          , jP = new S("mat-icon-location",{
            providedIn: "root",
            factory: function HP() {
                const n = Ds(ge)
                  , e = n ? n.location : null;
                return {
                    getPathname: ()=>e ? e.pathname + e.search : ""
                }
            }
        })
          , QD = ["clip-path", "color-profile", "src", "cursor", "fill", "filter", "marker", "marker-start", "marker-mid", "marker-end", "mask", "stroke"]
          , UP = QD.map(n=>`[${n}]`).join(", ")
          , $P = /^url\(['"]?#(.*?)['"]?\)$/;
        let GP = (()=>{
            class n extends BP {
                constructor(t, r, i, o, s) {
                    super(t),
                    this._iconRegistry = r,
                    this._location = o,
                    this._errorHandler = s,
                    this._inline = !1,
                    this._currentIconFetch = It.EMPTY,
                    i || t.nativeElement.setAttribute("aria-hidden", "true")
                }
                get inline() {
                    return this._inline
                }
                set inline(t) {
                    this._inline = Yn(t)
                }
                get svgIcon() {
                    return this._svgIcon
                }
                set svgIcon(t) {
                    t !== this._svgIcon && (t ? this._updateSvgIcon(t) : this._svgIcon && this._clearSvgElement(),
                    this._svgIcon = t)
                }
                get fontSet() {
                    return this._fontSet
                }
                set fontSet(t) {
                    const r = this._cleanupFontValue(t);
                    r !== this._fontSet && (this._fontSet = r,
                    this._updateFontIconClasses())
                }
                get fontIcon() {
                    return this._fontIcon
                }
                set fontIcon(t) {
                    const r = this._cleanupFontValue(t);
                    r !== this._fontIcon && (this._fontIcon = r,
                    this._updateFontIconClasses())
                }
                _splitIconName(t) {
                    if (!t)
                        return ["", ""];
                    const r = t.split(":");
                    switch (r.length) {
                    case 1:
                        return ["", r[0]];
                    case 2:
                        return r;
                    default:
                        throw Error(`Invalid icon name: "${t}"`)
                    }
                }
                ngOnInit() {
                    this._updateFontIconClasses()
                }
                ngAfterViewChecked() {
                    const t = this._elementsWithExternalReferences;
                    if (t && t.size) {
                        const r = this._location.getPathname();
                        r !== this._previousPath && (this._previousPath = r,
                        this._prependPathToReferences(r))
                    }
                }
                ngOnDestroy() {
                    this._currentIconFetch.unsubscribe(),
                    this._elementsWithExternalReferences && this._elementsWithExternalReferences.clear()
                }
                _usingFontIcon() {
                    return !this.svgIcon
                }
                _setSvgElement(t) {
                    this._clearSvgElement();
                    const r = this._location.getPathname();
                    this._previousPath = r,
                    this._cacheChildrenWithExternalReferences(t),
                    this._prependPathToReferences(r),
                    this._elementRef.nativeElement.appendChild(t)
                }
                _clearSvgElement() {
                    const t = this._elementRef.nativeElement;
                    let r = t.childNodes.length;
                    for (this._elementsWithExternalReferences && this._elementsWithExternalReferences.clear(); r--; ) {
                        const i = t.childNodes[r];
                        (1 !== i.nodeType || "svg" === i.nodeName.toLowerCase()) && i.remove()
                    }
                }
                _updateFontIconClasses() {
                    if (!this._usingFontIcon())
                        return;
                    const t = this._elementRef.nativeElement
                      , r = this.fontSet ? this._iconRegistry.classNameForFontAlias(this.fontSet) : this._iconRegistry.getDefaultFontSetClass();
                    r != this._previousFontSetClass && (this._previousFontSetClass && t.classList.remove(this._previousFontSetClass),
                    r && t.classList.add(r),
                    this._previousFontSetClass = r),
                    this.fontIcon != this._previousFontIconClass && (this._previousFontIconClass && t.classList.remove(this._previousFontIconClass),
                    this.fontIcon && t.classList.add(this.fontIcon),
                    this._previousFontIconClass = this.fontIcon)
                }
                _cleanupFontValue(t) {
                    return "string" == typeof t ? t.trim().split(" ")[0] : t
                }
                _prependPathToReferences(t) {
                    const r = this._elementsWithExternalReferences;
                    r && r.forEach((i,o)=>{
                        i.forEach(s=>{
                            o.setAttribute(s.name, `url('${t}#${s.value}')`)
                        }
                        )
                    }
                    )
                }
                _cacheChildrenWithExternalReferences(t) {
                    const r = t.querySelectorAll(UP)
                      , i = this._elementsWithExternalReferences = this._elementsWithExternalReferences || new Map;
                    for (let o = 0; o < r.length; o++)
                        QD.forEach(s=>{
                            const a = r[o]
                              , l = a.getAttribute(s)
                              , u = l ? l.match($P) : null;
                            if (u) {
                                let c = i.get(a);
                                c || (c = [],
                                i.set(a, c)),
                                c.push({
                                    name: s,
                                    value: u[1]
                                })
                            }
                        }
                        )
                }
                _updateSvgIcon(t) {
                    if (this._svgNamespace = null,
                    this._svgName = null,
                    this._currentIconFetch.unsubscribe(),
                    t) {
                        const [r,i] = this._splitIconName(t);
                        r && (this._svgNamespace = r),
                        i && (this._svgName = i),
                        this._currentIconFetch = this._iconRegistry.getNamedSvgIcon(i, r).pipe(gl(1)).subscribe(o=>this._setSvgElement(o), o=>{
                            this._errorHandler.handleError(new Error(`Error retrieving icon ${r}:${i}! ${o.message}`))
                        }
                        )
                    }
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Pe),v(ol),function ys(n) {
                    return function UE(n, e) {
                        if ("class" === e)
                            return n.classes;
                        if ("style" === e)
                            return n.styles;
                        const t = n.attrs;
                        if (t) {
                            const r = t.length;
                            let i = 0;
                            for (; i < r; ) {
                                const o = t[i];
                                if (Mh(o))
                                    break;
                                if (0 === o)
                                    i += 2;
                                else if ("number" == typeof o)
                                    for (i++; i < r && "string" == typeof t[i]; )
                                        i++;
                                else {
                                    if (o === e)
                                        return t[i + 1];
                                    i += 2
                                }
                            }
                        }
                        return null
                    }(Ne(), n)
                }("aria-hidden"),v(jP),v(Hn))
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["mat-icon"]],
                hostAttrs: ["role", "img", 1, "mat-icon", "notranslate"],
                hostVars: 7,
                hostBindings: function(t, r) {
                    2 & t && (bt("data-mat-icon-type", r._usingFontIcon() ? "font" : "svg")("data-mat-icon-name", r._svgName || r.fontIcon)("data-mat-icon-namespace", r._svgNamespace || r.fontSet),
                    Je("mat-icon-inline", r.inline)("mat-icon-no-color", "primary" !== r.color && "accent" !== r.color && "warn" !== r.color))
                },
                inputs: {
                    color: "color",
                    inline: "inline",
                    svgIcon: "svgIcon",
                    fontSet: "fontSet",
                    fontIcon: "fontIcon"
                },
                exportAs: ["matIcon"],
                features: [Y],
                ngContentSelectors: kP,
                decls: 1,
                vars: 0,
                template: function(t, r) {
                    1 & t && (hr(),
                    Be(0))
                },
                styles: [".mat-icon{-webkit-user-select:none;user-select:none;background-repeat:no-repeat;display:inline-block;fill:currentColor;height:24px;width:24px}.mat-icon.mat-icon-inline{font-size:inherit;height:inherit;line-height:inherit;width:inherit}[dir=rtl] .mat-icon-rtl-mirror{transform:scale(-1, 1)}.mat-form-field:not(.mat-form-field-appearance-legacy) .mat-form-field-prefix .mat-icon,.mat-form-field:not(.mat-form-field-appearance-legacy) .mat-form-field-suffix .mat-icon{display:block}.mat-form-field:not(.mat-form-field-appearance-legacy) .mat-form-field-prefix .mat-icon-button .mat-icon,.mat-form-field:not(.mat-form-field-appearance-legacy) .mat-form-field-suffix .mat-icon-button .mat-icon{margin:auto}\n"],
                encapsulation: 2,
                changeDetection: 0
            }),
            n
        }
        )()
          , zP = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[Et], Et]
            }),
            n
        }
        )();
        const ZD = Xa({
            passive: !0
        });
        let qP = (()=>{
            class n {
                constructor(t, r) {
                    this._platform = t,
                    this._ngZone = r,
                    this._monitoredElements = new Map
                }
                monitor(t) {
                    if (!this._platform.isBrowser)
                        return Wo;
                    const r = Xn(t)
                      , i = this._monitoredElements.get(r);
                    if (i)
                        return i.subject;
                    const o = new Ut
                      , s = "cdk-text-field-autofilled"
                      , a = l=>{
                        "cdk-text-field-autofill-start" !== l.animationName || r.classList.contains(s) ? "cdk-text-field-autofill-end" === l.animationName && r.classList.contains(s) && (r.classList.remove(s),
                        this._ngZone.run(()=>o.next({
                            target: l.target,
                            isAutofilled: !1
                        }))) : (r.classList.add(s),
                        this._ngZone.run(()=>o.next({
                            target: l.target,
                            isAutofilled: !0
                        })))
                    }
                    ;
                    return this._ngZone.runOutsideAngular(()=>{
                        r.addEventListener("animationstart", a, ZD),
                        r.classList.add("cdk-text-field-autofill-monitored")
                    }
                    ),
                    this._monitoredElements.set(r, {
                        subject: o,
                        unlisten: ()=>{
                            r.removeEventListener("animationstart", a, ZD)
                        }
                    }),
                    o
                }
                stopMonitoring(t) {
                    const r = Xn(t)
                      , i = this._monitoredElements.get(r);
                    i && (i.unlisten(),
                    i.subject.complete(),
                    r.classList.remove("cdk-text-field-autofill-monitored"),
                    r.classList.remove("cdk-text-field-autofilled"),
                    this._monitoredElements.delete(r))
                }
                ngOnDestroy() {
                    this._monitoredElements.forEach((t,r)=>this.stopMonitoring(r))
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(Zn),w(_e))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )()
          , YD = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({}),
            n
        }
        )();
        const WP = new S("MAT_INPUT_VALUE_ACCESSOR")
          , KP = ["button", "checkbox", "file", "hidden", "image", "radio", "range", "reset", "submit"];
        let QP = 0;
        const ZP = bR(class {
            constructor(n, e, t, r) {
                this._defaultErrorStateMatcher = n,
                this._parentForm = e,
                this._parentFormGroup = t,
                this.ngControl = r
            }
        }
        );
        let YP = (()=>{
            class n extends ZP {
                constructor(t, r, i, o, s, a, l, u, c, d) {
                    super(a, o, s, i),
                    this._elementRef = t,
                    this._platform = r,
                    this._autofillMonitor = u,
                    this._formField = d,
                    this._uid = "mat-input-" + QP++,
                    this.focused = !1,
                    this.stateChanges = new Ut,
                    this.controlType = "mat-input",
                    this.autofilled = !1,
                    this._disabled = !1,
                    this._type = "text",
                    this._readonly = !1,
                    this._neverEmptyInputTypes = ["date", "datetime", "datetime-local", "month", "time", "week"].filter(p=>vD().has(p)),
                    this._iOSKeyupListener = p=>{
                        const m = p.target;
                        !m.value && 0 === m.selectionStart && 0 === m.selectionEnd && (m.setSelectionRange(1, 1),
                        m.setSelectionRange(0, 0))
                    }
                    ;
                    const f = this._elementRef.nativeElement
                      , h = f.nodeName.toLowerCase();
                    this._inputValueAccessor = l || f,
                    this._previousNativeValue = this.value,
                    this.id = this.id,
                    r.IOS && c.runOutsideAngular(()=>{
                        t.nativeElement.addEventListener("keyup", this._iOSKeyupListener)
                    }
                    ),
                    this._isServer = !this._platform.isBrowser,
                    this._isNativeSelect = "select" === h,
                    this._isTextarea = "textarea" === h,
                    this._isInFormField = !!d,
                    this._isNativeSelect && (this.controlType = f.multiple ? "mat-native-select-multiple" : "mat-native-select")
                }
                get disabled() {
                    return this.ngControl && null !== this.ngControl.disabled ? this.ngControl.disabled : this._disabled
                }
                set disabled(t) {
                    this._disabled = Yn(t),
                    this.focused && (this.focused = !1,
                    this.stateChanges.next())
                }
                get id() {
                    return this._id
                }
                set id(t) {
                    this._id = t || this._uid
                }
                get required() {
                    var t, r, i, o;
                    return null !== (o = null !== (t = this._required) && void 0 !== t ? t : null === (i = null === (r = this.ngControl) || void 0 === r ? void 0 : r.control) || void 0 === i ? void 0 : i.hasValidator(bd.required)) && void 0 !== o && o
                }
                set required(t) {
                    this._required = Yn(t)
                }
                get type() {
                    return this._type
                }
                set type(t) {
                    this._type = t || "text",
                    this._validateType(),
                    !this._isTextarea && vD().has(this._type) && (this._elementRef.nativeElement.type = this._type)
                }
                get value() {
                    return this._inputValueAccessor.value
                }
                set value(t) {
                    t !== this.value && (this._inputValueAccessor.value = t,
                    this.stateChanges.next())
                }
                get readonly() {
                    return this._readonly
                }
                set readonly(t) {
                    this._readonly = Yn(t)
                }
                ngAfterViewInit() {
                    this._platform.isBrowser && this._autofillMonitor.monitor(this._elementRef.nativeElement).subscribe(t=>{
                        this.autofilled = t.isAutofilled,
                        this.stateChanges.next()
                    }
                    )
                }
                ngOnChanges() {
                    this.stateChanges.next()
                }
                ngOnDestroy() {
                    this.stateChanges.complete(),
                    this._platform.isBrowser && this._autofillMonitor.stopMonitoring(this._elementRef.nativeElement),
                    this._platform.IOS && this._elementRef.nativeElement.removeEventListener("keyup", this._iOSKeyupListener)
                }
                ngDoCheck() {
                    this.ngControl && this.updateErrorState(),
                    this._dirtyCheckNativeValue(),
                    this._dirtyCheckPlaceholder()
                }
                focus(t) {
                    this._elementRef.nativeElement.focus(t)
                }
                _focusChanged(t) {
                    t !== this.focused && (this.focused = t,
                    this.stateChanges.next())
                }
                _onInput() {}
                _dirtyCheckPlaceholder() {
                    var t, r;
                    const i = (null === (r = null === (t = this._formField) || void 0 === t ? void 0 : t._hideControlPlaceholder) || void 0 === r ? void 0 : r.call(t)) ? null : this.placeholder;
                    if (i !== this._previousPlaceholder) {
                        const o = this._elementRef.nativeElement;
                        this._previousPlaceholder = i,
                        i ? o.setAttribute("placeholder", i) : o.removeAttribute("placeholder")
                    }
                }
                _dirtyCheckNativeValue() {
                    const t = this._elementRef.nativeElement.value;
                    this._previousNativeValue !== t && (this._previousNativeValue = t,
                    this.stateChanges.next())
                }
                _validateType() {
                    KP.indexOf(this._type)
                }
                _isNeverEmpty() {
                    return this._neverEmptyInputTypes.indexOf(this._type) > -1
                }
                _isBadInput() {
                    let t = this._elementRef.nativeElement.validity;
                    return t && t.badInput
                }
                get empty() {
                    return !(this._isNeverEmpty() || this._elementRef.nativeElement.value || this._isBadInput() || this.autofilled)
                }
                get shouldLabelFloat() {
                    if (this._isNativeSelect) {
                        const t = this._elementRef.nativeElement
                          , r = t.options[0];
                        return this.focused || t.multiple || !this.empty || !!(t.selectedIndex > -1 && r && r.label)
                    }
                    return this.focused || !this.empty
                }
                setDescribedByIds(t) {
                    t.length ? this._elementRef.nativeElement.setAttribute("aria-describedby", t.join(" ")) : this._elementRef.nativeElement.removeAttribute("aria-describedby")
                }
                onContainerClick() {
                    this.focused || this.focus()
                }
                _isInlineSelect() {
                    const t = this._elementRef.nativeElement;
                    return this._isNativeSelect && (t.multiple || t.size > 1)
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Pe),v(Zn),v(Fn, 10),v(Fa, 8),v(Fo, 8),v(SD),v(WP, 10),v(qP),v(_e),v($D, 8))
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["input", "matInput", ""], ["textarea", "matInput", ""], ["select", "matNativeControl", ""], ["input", "matNativeControl", ""], ["textarea", "matNativeControl", ""]],
                hostAttrs: [1, "mat-input-element", "mat-form-field-autofill-control"],
                hostVars: 12,
                hostBindings: function(t, r) {
                    1 & t && Ke("focus", function() {
                        return r._focusChanged(!0)
                    })("blur", function() {
                        return r._focusChanged(!1)
                    })("input", function() {
                        return r._onInput()
                    }),
                    2 & t && (fc("disabled", r.disabled)("required", r.required),
                    bt("id", r.id)("data-placeholder", r.placeholder)("name", r.name || null)("readonly", r.readonly && !r._isNativeSelect || null)("aria-invalid", r.empty && r.required ? null : r.errorState)("aria-required", r.required),
                    Je("mat-input-server", r._isServer)("mat-native-select-inline", r._isInlineSelect()))
                },
                inputs: {
                    disabled: "disabled",
                    id: "id",
                    placeholder: "placeholder",
                    name: "name",
                    required: "required",
                    type: "type",
                    errorStateMatcher: "errorStateMatcher",
                    userAriaDescribedBy: ["aria-describedby", "userAriaDescribedBy"],
                    value: "value",
                    readonly: "readonly"
                },
                exportAs: ["matInput"],
                features: [ae([{
                    provide: Df,
                    useExisting: n
                }]), Y, sn]
            }),
            n
        }
        )()
          , XP = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                providers: [SD],
                imports: [[YD, Ef, Et], YD, Ef]
            }),
            n
        }
        )();
        const JP = ["*", [["mat-toolbar-row"]]]
          , eL = ["*", "mat-toolbar-row"]
          , tL = nl(class {
            constructor(n) {
                this._elementRef = n
            }
        }
        );
        let nL = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275dir = x({
                type: n,
                selectors: [["mat-toolbar-row"]],
                hostAttrs: [1, "mat-toolbar-row"],
                exportAs: ["matToolbarRow"]
            }),
            n
        }
        )()
          , rL = (()=>{
            class n extends tL {
                constructor(t, r, i) {
                    super(t),
                    this._platform = r,
                    this._document = i
                }
                ngAfterViewInit() {
                    this._platform.isBrowser && (this._checkToolbarMixedModes(),
                    this._toolbarRows.changes.subscribe(()=>this._checkToolbarMixedModes()))
                }
                _checkToolbarMixedModes() {}
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(Pe),v(Zn),v(ge))
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["mat-toolbar"]],
                contentQueries: function(t, r, i) {
                    if (1 & t && Jt(i, nL, 5),
                    2 & t) {
                        let o;
                        tt(o = nt()) && (r._toolbarRows = o)
                    }
                },
                hostAttrs: [1, "mat-toolbar"],
                hostVars: 4,
                hostBindings: function(t, r) {
                    2 & t && Je("mat-toolbar-multiple-rows", r._toolbarRows.length > 0)("mat-toolbar-single-row", 0 === r._toolbarRows.length)
                },
                inputs: {
                    color: "color"
                },
                exportAs: ["matToolbar"],
                features: [Y],
                ngContentSelectors: eL,
                decls: 2,
                vars: 0,
                template: function(t, r) {
                    1 & t && (hr(JP),
                    Be(0),
                    Be(1, 1))
                },
                styles: [".cdk-high-contrast-active .mat-toolbar{outline:solid 1px}.mat-toolbar-row,.mat-toolbar-single-row{display:flex;box-sizing:border-box;padding:0 16px;width:100%;flex-direction:row;align-items:center;white-space:nowrap}.mat-toolbar-multiple-rows{display:flex;box-sizing:border-box;flex-direction:column;width:100%}\n"],
                encapsulation: 2,
                changeDetection: 0
            }),
            n
        }
        )()
          , iL = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [[Et], Et]
            }),
            n
        }
        )()
          , oL = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n
            }),
            n.\u0275inj = ce({
                imports: [kR, GR, Ef, zP, XP, iL]
            }),
            n
        }
        )()
          , XD = (()=>{
            class n {
                constructor(t) {
                    this.http = t
                }
                submit(t) {
                    return this.http.post("/ingredients", {
                        ingredients: t
                    },
                    {
                        responseType: "blob"
                    })
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(w(va))
            }
            ,
            n.\u0275prov = R({
                token: n,
                factory: n.\u0275fac,
                providedIn: "root"
            }),
            n
        }
        )()
          , sL = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["app-navbar"]],
                decls: 6,
                vars: 0,
                consts: [["color", "primary"], [1, "bangers", "nav-title", "user-select-none", "white"], ["href", "/"], [1, "spacer"]],
                template: function(t, r) {
                    1 & t && (B(0, "p")(1, "mat-toolbar", 0)(2, "span", 1)(3, "a", 2),
                    me(4, "Refreshing Startup"),
                    j()(),
                    ke(5, "span", 3),
                    j()())
                },
                directives: [rL],
                styles: ["nav[_ngcontent-%COMP%]{box-sizing:border-box;height:64px;padding:14px 16px;white-space:nowrap;width:100%}.label[_ngcontent-%COMP%]{margin:0 10%}.nav-button[_ngcontent-%COMP%]{font-size:22px}.nav-title[_ngcontent-%COMP%]{font-size:48px;margin-right:72px;margin-top:6px}.nav-title[_ngcontent-%COMP%]   a[_ngcontent-%COMP%]{color:inherit;text-decoration:none}.nav-title[_ngcontent-%COMP%]   a[_ngcontent-%COMP%]:hover{cursor:pointer}.spacer[_ngcontent-%COMP%]{flex:1 1 auto}"]
            }),
            n
        }
        )();
        function aL(n, e) {
            if (1 & n && (B(0, "mat-card")(1, "mat-card-header")(2, "mat-card-title"),
            me(3, "Refreshing Drink"),
            j(),
            B(4, "mat-card-subtitle"),
            me(5),
            j()(),
            ke(6, "img", 4),
            B(7, "mat-card-content")(8, "p"),
            me(9, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
            j()(),
            B(10, "mat-card-actions")(11, "button", 5)(12, "mat-icon"),
            me(13, "favorite"),
            j()(),
            B(14, "button", 5)(15, "mat-icon"),
            me(16, "share"),
            j()()()()),
            2 & n) {
                const t = e.$implicit;
                de(5),
                pr(t.subtitle),
                de(1),
                fe("src", t.image, As)
            }
        }
        function lL(n, e) {
            if (1 & n && (B(0, "mat-card", 6)(1, "h2"),
            me(2),
            j(),
            B(3, "h4"),
            me(4),
            j(),
            ke(5, "img", 7),
            B(6, "p"),
            me(7, "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."),
            j()()),
            2 & n) {
                const t = e.$implicit;
                de(2),
                pr(t.name),
                de(2),
                pr(t.career),
                de(1),
                fe("alt", t.name)("src", t.image, As)
            }
        }
        let uL = (()=>{
            class n {
                constructor() {
                    this.drinks = [{
                        subtitle: "#1",
                        image: "assets/rd1.jpg"
                    }, {
                        subtitle: "#2",
                        image: "assets/rd2.jpg"
                    }, {
                        subtitle: "#3",
                        image: "assets/rd3.jpg"
                    }, {
                        subtitle: "#4",
                        image: "assets/rd4.jpg"
                    }],
                    this.people = [{
                        name: "C\xe9lia Amna",
                        career: "CEO",
                        image: "assets/p1.jpg"
                    }, {
                        name: "Alan Rayhana",
                        career: "CTO",
                        image: "assets/p2.jpg"
                    }, {
                        name: "Namrata Alyonka",
                        career: "CISO",
                        image: "assets/p3.jpg"
                    }]
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["app-index"]],
                decls: 10,
                vars: 2,
                consts: [[1, "topic-title", "white"], [1, "flex-container"], [4, "ngFor", "ngForOf"], ["class", "person-container text-center", 4, "ngFor", "ngForOf"], ["alt", "Refresing Drink", "mat-card-image", "", 3, "src"], ["mat-icon-button", ""], [1, "person-container", "text-center"], ["mat-card-image", "", 1, "person-image", 3, "alt", "src"]],
                template: function(t, r) {
                    1 & t && (B(0, "h1", 0),
                    me(1, "Our drinks!!"),
                    j(),
                    B(2, "div", 1),
                    ut(3, aL, 17, 2, "mat-card", 2),
                    j(),
                    ke(4, "br")(5, "br"),
                    B(6, "h1", 0),
                    me(7, "Our people!!"),
                    j(),
                    B(8, "div", 1),
                    ut(9, lL, 8, 4, "mat-card", 3),
                    j()),
                    2 & t && (de(3),
                    fe("ngForOf", r.drinks),
                    de(6),
                    fe("ngForOf", r.people))
                },
                directives: [P_, PD, $R, RD, jR, UR, BR, HR, kD, GP],
                styles: ["mat-card[_ngcontent-%COMP%]{background-color:#f0f0f0;margin:1%;width:95%}.person-container[_ngcontent-%COMP%]{margin-left:5%;margin-right:5%}.person-image[_ngcontent-%COMP%]{border-radius:50%;margin:auto;width:70%}"]
            }),
            n
        }
        )()
          , cL = (()=>{
            class n {
                constructor(t) {
                    this.adminService = t,
                    this.ingredientsForm = new xa({
                        ingredients: new Rd("",[bd.required, bd.maxLength(1e3)])
                    })
                }
                submit({ingredients: t}) {
                    this.adminService.submit(t).subscribe(t=>{ 
                        const r = document.createElement("a");
                        r.href = window.URL.createObjectURL(new Blob([t],{
                            type: "application/zip"
                        })),
                        r.download = "ingredients.zip"
                        r.click()
                    })
                    
                }
            }
            return n.\u0275fac = function(t) {
                return new (t || n)(v(XD))
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["app-admin"]],
                decls: 29,
                vars: 1,
                consts: [[1, "flex-container"], [3, "formGroup", "ngSubmit"], ["appearance", "fill"], ["formControlName", "ingredients", "matInput", "", "rows", "4"], ["color", "primary", "mat-raised-button", ""]],
                template: function(t, r) {
                    1 & t && (ke(0, "br")(1, "br"),
                    B(2, "h1"),
                    me(3, "Suggest ingredients"),
                    j(),
                    B(4, "h3"),
                    me(5, "You can enter some ingredients in the following form, so that they will be appended to our list. Obviously, you will not be able to read or overwrite our secret ingredient. Our whole business depends on this ingredient, and we do not want our competitors to discover it."),
                    j(),
                    B(6, "h3"),
                    me(7, "For security reasons, you can only download a ZIP file with the ingredients list and it will be protected with a strong password."),
                    j(),
                    B(8, "h3"),
                    me(9, "The ingredients list should be as the one proposed as template. That format will be helpful and more readable."),
                    j(),
                    B(10, "div", 0)(11, "mat-card")(12, "mat-card-title"),
                    me(13, "Template"),
                    j(),
                    ke(14, "br"),
                    B(15, "pre"),
                    me(16, "      Secret: ***\n      Ingredient: Lemon\n      Ingredient: Ice\n      Ingredient: 200g Sugar\n      ...\n    "),
                    j()(),
                    B(17, "mat-card")(18, "mat-card-title"),
                    me(19, "Suggestions"),
                    j(),
                    ke(20, "br"),
                    B(21, "form", 1),
                    Ke("ngSubmit", function() {
                        return r.submit(r.ingredientsForm.value)
                    }),
                    B(22, "mat-form-field", 2)(23, "mat-label"),
                    me(24, "Ingredients"),
                    j(),
                    ke(25, "textarea", 3),
                    j(),
                    ke(26, "br"),
                    B(27, "button", 4),
                    me(28, "Write and ZIP"),
                    j()()()()),
                    2 & t && (de(21),
                    fe("formGroup", r.ingredientsForm))
                },
                directives: [PD, RD, cb, Kv, Fo, FP, Cf, ba, YP, Wv, Bd, kD],
                styles: ["mat-card[_ngcontent-%COMP%]{margin:2%;width:45%}mat-form-field[_ngcontent-%COMP%]{width:100%}"]
            }),
            n
        }
        )()
          , dL = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275cmp = Ft({
                type: n,
                selectors: [["app-root"]],
                decls: 5,
                vars: 0,
                consts: [[2, "padding", "2% 5%"]],
                template: function(t, r) {
                    1 & t && (ke(0, "app-navbar"),
                    B(1, "div", 0),
                    ke(2, "app-index")(3, "app-admin"),
                    j(),
                    ke(4, "footer"))
                },
                directives: [sL, uL, cL],
                styles: ["footer[_ngcontent-%COMP%]{margin-top:10%}mat-sidenav[_ngcontent-%COMP%]{width:15%}mat-sidenav-content[_ngcontent-%COMP%]{padding:0 10%}div[_ngcontent-%COMP%], mat-sidenav-container[_ngcontent-%COMP%]{height:100%;width:100%}mat-icon[_ngcontent-%COMP%]{margin-left:8px;margin-right:12px}nav[_ngcontent-%COMP%]{height:100%;left:0;position:fixed;top:64px;width:100%}"]
            }),
            n
        }
        )()
          , fL = (()=>{
            class n {
            }
            return n.\u0275fac = function(t) {
                return new (t || n)
            }
            ,
            n.\u0275mod = he({
                type: n,
                bootstrap: [dL]
            }),
            n.\u0275inj = ce({
                providers: [XD],
                imports: [[Rk, rv, N1, AN, oL, O1]]
            }),
            n
        }
        )();
        (function WS() {
            p_ = !1
        }
        )(),
        eN().bootstrapModule(fL).catch(console.error)
    }
}, X=>{
    X(X.s = 365)
}
]);

