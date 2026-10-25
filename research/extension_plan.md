# Phase 7 — calibration-shift diagnosis

**[Experimental observation]** Frozen v1 primary criterion failed: common-cause CMI minus MI FPR = +.070, bootstrap interval [.048,.092]. Stochastic-channel recall was 500/500.

**[Hypothesis]** Biggest interpretability weakness: the test action-noise shift changes both the signal and finite-sample null distribution, so the original comparison cannot tell whether context conditioning is intrinsically unhelpful or the operating threshold failed to transport.

**[Future work — recorded after v1, before extension run]** Run the identical pipeline with held-out noise .1 instead of .25. Keep seeds, train/calibration data, features, target FPR, threshold rule and all stress conditions unchanged. This is an exploratory same-distribution diagnostic, not a replacement final test or an additional confirmatory success claim. Test RNG streams remain separate; reuse of test scenarios means the extension is not independently preregistered. Save all results alongside v1.
