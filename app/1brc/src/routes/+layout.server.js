import { VERCEL_ENV, BEAM_KEY } from '$env/static/private';

export function load() {
    return {
        deploymentEnv: VERCEL_ENV,
        beamKey: BEAM_KEY,
    };
}