% for highlight in highlights:
<div
  class="space-y-4 md:space-y-6 h-full flex flex-col justify-start items-center text-center"
>
  <img
    class="h-28 md:h-40"
    src="/assets/illustrations/{{ highlight['illustration'] }}"
    alt="{{ highlight['illustration_alt'] }}"
  />
  <div class="space-y-3">
    <h4 class="">{{ highlight["title"] }}</h4>
    <p class="text-base text-unidDarkBlue">{{ highlight["text"] }}</p>
  </div>
</div>
% end
