/**
 * htmx-ext-sse reconnects after EventSource.close() and on connection errors.
 * Remove sse-connect so scheduled retries are no-ops.
 *
 * - htmx:sseClose (type "message"): server sent sse-close event (e.g. order delivered)
 * - htmx:sseError: connection failed (e.g. HTTP 404) — EventSource never gets sse-close
 */

/** @typedef {"message" | "nodeMissing" | "nodeReplaced"} SseCloseReason */

/**
 * @typedef {object} HtmxSseCloseDetail
 * @property {HTMLElement} [elt]
 * @property {EventSource} source
 * @property {SseCloseReason} type
 */

/**
 * @typedef {object} HtmxSseErrorDetail
 * @property {HTMLElement} [elt]
 * @property {Event} error
 * @property {EventSource} source
 */

/** @typedef {CustomEvent<HtmxSseCloseDetail>} HtmxSseCloseEvent */

/** @typedef {CustomEvent<HtmxSseErrorDetail>} HtmxSseErrorEvent */

/**
 * @param {HtmxSseCloseEvent | HtmxSseErrorEvent} e
 * @returns {HTMLElement | null}
 */
function sseHostFromEvent(e) {
  if (e.detail.elt instanceof HTMLElement) return e.detail.elt;
  if (e.target instanceof HTMLElement) return e.target;
  return null;
}

/**
 * @param {HTMLElement | null} elt
 * @param {EventSource | undefined} source
 */
function stopSseReconnect(elt, source) {
  if (!elt) return;
  elt.removeAttribute("sse-connect");
  elt.removeAttribute("data-sse-connect");
  source?.close();
}

/** @param {HtmxSseCloseEvent} e */
function onSseClose(e) {
  if (e.detail.type !== "message") return;
  stopSseReconnect(sseHostFromEvent(e), e.detail.source);
}

/** @param {HtmxSseErrorEvent} e */
function onSseError(e) {
  stopSseReconnect(sseHostFromEvent(e), e.detail.source);
}

function install() {
  // Must use `document`, not `document.body` — this file may load from <head> before <body> exists.
  document.addEventListener("htmx:sseClose", onSseClose);
  document.addEventListener("htmx:sseError", onSseError);
}

install();
