/**
 * 연관된 근처 관광지 추천 슬라이드 컨트롤 스크립트
 */
if (typeof window.slideNearbyTrack === 'undefined') {
  window.slideNearbyTrack = function(trackId, dir) {
    var track = document.getElementById(trackId);
    if (!track) return;
    var firstCard = track.querySelector('.nearby-slide-card');
    var cardWidth = firstCard ? (firstCard.offsetWidth + 16) : 280;
    var count = (window.innerWidth < 650) ? 1 : (window.innerWidth < 992 ? 2 : 3);
    track.scrollBy({ left: dir * cardWidth * count, behavior: 'smooth' });
  };
}
